from pathlib import Path
import csv
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "published"
OUT = ROOT / "figures" / "regenerated"
OUT.mkdir(parents=True, exist_ok=True)

def read_csv(name):
    with (DATA/name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# Figure 3: charger allocation comparison
rows = [r for r in read_csv("table_III_charger_allocation.csv") if r["station"] != "Total"]
stations = [r["station"] for r in rows]
x = list(range(len(stations)))
width = 0.24

for method, prefix, title, fname in [
    ("B&C", "bc", "B&C charger allocation", "fig03a_bc_charger_allocation.png"),
    ("BIPSO-GR", "bipso_gr", "BIPSO-GR charger allocation", "fig03b_bipso_gr_charger_allocation.png"),
]:
    fig, ax = plt.subplots(figsize=(8,4.5))
    a=[float(r[f"{prefix}_11kw"]) for r in rows]
    b=[float(r[f"{prefix}_60kw"]) for r in rows]
    c=[float(r[f"{prefix}_150kw"]) for r in rows]
    ax.bar([i-width for i in x], a, width=width, label="11 kW")
    ax.bar(x, b, width=width, label="60 kW")
    ax.bar([i+width for i in x], c, width=width, label="150 kW")
    ax.set_xticks(x, stations)
    ax.set_ylabel("Number of chargers")
    ax.set_xlabel("Charging station")
    ax.set_title(title)
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUT/fname, dpi=300, bbox_inches="tight")
    plt.close(fig)

# Figure 5: Dmax sensitivity. Use separate figures for the count and distance metrics
# to avoid dual-axis ambiguity while preserving all published values.
rows=read_csv("table_VI_dmax_sensitivity.csv")
d=[float(r["dmax_km"]) for r in rows]
count=[float(r["stations_receiving_load"]) for r in rows]
avg=[float(r["average_used_distance_km"]) for r in rows]
mx=[float(r["max_used_distance_km"]) for r in rows]

fig, ax = plt.subplots(figsize=(6.5,4.2))
ax.plot(d,count,marker="o")
ax.set_xlabel(r"$D_{max}$ (km)")
ax.set_ylabel("Stations receiving load")
ax.set_xticks(d)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(OUT/"fig05a_dmax_loaded_stations.png",dpi=300,bbox_inches="tight")
plt.close(fig)

fig, ax = plt.subplots(figsize=(6.5,4.2))
ax.plot(d,avg,marker="o",label="Average used distance")
ax.plot(d,mx,marker="s",label="Maximum used distance")
ax.set_xlabel(r"$D_{max}$ (km)")
ax.set_ylabel("Used assignment distance (km)")
ax.set_xticks(d)
ax.legend(frameon=False)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(OUT/"fig05b_dmax_used_distances.png",dpi=300,bbox_inches="tight")
plt.close(fig)

print("Figure regeneration: PASS")
