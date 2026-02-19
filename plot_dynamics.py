"""
plot_dynamics.py — Reads audit_log.json produced by certified_dynamics.py
and generates a 2D chart showing how the system state collides with the
regulatory barrier over simulated time.

Usage:
    python plot_dynamics.py [audit_log.json]
"""

import json
import sys
import os

try:
    import matplotlib
    matplotlib.use("Agg")  # Non-interactive backend for headless environments
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
except ImportError:
    sys.exit(
        "matplotlib is required to run this script.\n"
        "Install it with:  pip install matplotlib"
    )


# ── colour mapping for admissibility statuses ──────────────────────────
STATUS_COLOURS = {
    "FULLY_ADMISSIBLE":   "#2ecc71",   # green
    "MIXED_BOUNDARY":     "#f39c12",   # orange
    "INADMISSIBLE":       "#e74c3c",   # red
    "CONDITIONAL_PENDING": "#3498db",  # blue
}


def load_audit_log(filepath: str) -> list:
    """Load and return the audit log entries from a JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)


def plot_audit_log(entries: list, output_path: str = "dynamics_plot.png"):
    """
    Generate a 2D scatter/line plot:
      • X-axis  → simulation_time
      • Y-axis  → first element of state_vector (e.g. dB)
      • Colour  → admissibility status
    """
    times = [e["simulation_time"] for e in entries]
    values = [e["state_vector"][0] for e in entries]
    statuses = [e["status"] for e in entries]
    colours = [STATUS_COLOURS.get(s, "#95a5a6") for s in statuses]

    fig, ax = plt.subplots(figsize=(10, 5))

    # Line connecting all points
    ax.plot(times, values, linestyle="--", color="#bdc3c7", linewidth=1, zorder=1)

    # Scatter coloured by status
    ax.scatter(times, values, c=colours, s=90, edgecolors="black",
               linewidths=0.6, zorder=2)

    # Legend
    patches = [
        mpatches.Patch(color=c, label=s.replace("_", " ").title())
        for s, c in STATUS_COLOURS.items()
    ]
    ax.legend(handles=patches, loc="upper left", fontsize=8, framealpha=0.9)

    ax.set_xlabel("Simulation Time (years)")
    ax.set_ylabel("State (dB)")
    ax.set_title("Certified Dynamics — State vs. Regulatory Barrier")
    ax.grid(True, linestyle=":", alpha=0.5)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    print(f"[Plot] Chart saved to {output_path}")
    plt.close(fig)


# ── entry point ────────────────────────────────────────────────────────
if __name__ == "__main__":
    log_file = sys.argv[1] if len(sys.argv) > 1 else "audit_log.json"

    if not os.path.isfile(log_file):
        sys.exit(
            f"Audit log not found: {log_file}\n"
            "Run  python certified_dynamics.py  first to generate it."
        )

    entries = load_audit_log(log_file)
    plot_audit_log(entries)
