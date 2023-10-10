
def gefühlteTemperatur(T, v):
    Tf = 13.12 + 0.6215 * T + (0.3965 * T - 11.37) * (v **0.16)
    print(Tf)

gefühlteTemperatur(32, 40)