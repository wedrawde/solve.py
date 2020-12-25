# Solve:
#    LETA
#   +TALL
#   =====
#   CACHE

for a in range(10):
  for e in range(10):
    for l in range(10):
      for t in range(10):
        for c in range(10):
          for h in range(10):
            if int(f"{l}{e}{t}{a}") + int(f"{t}{a}{l}{l}") == int(f"{c}{a}{c}{h}{e}"):
              print(f"{l}{e}{t}{a} + {t}{a}{l}{l} = {c}{a}{c}{h}{e}")
