from random import randint


def turrets_generator():
    def shoot() -> str:
        return "Shooting"

    def search() -> str:
        return "Searching"

    def talk() -> str:
        return "Talking"

    for _ in range(5):
        neuroticism: int = randint(0, 100)
        openness: int = randint(0, 100 - neuroticism)
        conscientiousness: int = randint(0, 100 - neuroticism - openness)
        extraversion: int = randint(0, 100 - neuroticism - openness - conscientiousness)
        agreeableness: int = 100 - neuroticism - openness - conscientiousness - extraversion

        attrs = {
            "neuroticism": neuroticism,
            "openness": openness,
            "conscientiousness": conscientiousness,
            "extraversion": extraversion,
            "agreeableness": agreeableness,

            "shoot": shoot,
            "search": search,
            "talk": talk
        }
        yield type("Turret", (object,), attrs)


def main():
    for i, turret in enumerate(turrets_generator()):
        print(f"turret {i}")
        print(f"neuroticism = {turret.neuroticism}")
        print(f"openness = {turret.openness}")
        print(f"conscientiousness = {turret.conscientiousness}")
        print(f"extraversion = {turret.extraversion}")
        print(f"agreeableness = {turret.agreeableness}")
        print("sum =",
              turret.neuroticism +
              turret.openness +
              turret.conscientiousness +
              turret.extraversion +
              turret.agreeableness)
        print(turret.shoot())
        print(turret.search())
        print(turret.talk(), end='\n\n')


if __name__ == "__main__":
    main()
