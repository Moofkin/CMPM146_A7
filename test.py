import subprocess

CLINGO = "clingo"
args = ["level-core.lp", "level-style.lp", "level-sim.lp"]

clingo = subprocess.Popen(
    "gringo level-core.lp level-style.lp level-sim.lp level-shortcuts.lp | reify | clingo - meta.lp metaD.lp metaO.lp metaS.lp --parallel-mode=4 --outf=2",
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
out, err = clingo.communicate()
print out
print err