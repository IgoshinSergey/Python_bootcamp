import asyncio

from enum import Enum, auto
from random import choice, shuffle, uniform
from typing import Dict, List


class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()


class Agent:

    def __aiter__(self, health=5):
        self.health = health
        self.actions = list(Action)
        return self

    async def __anext__(self):
        return choice(self.actions)


async def get_neo_action(agent_action: Action) -> Action:
    neo_actions: Dict[Action, Action] = {
        Action.HIGHKICK: Action.HIGHBLOCK,
        Action.HIGHBLOCK: Action.HIGHKICK,
        Action.LOWKICK: Action.LOWBLOCK,
        Action.LOWBLOCK: Action.LOWKICK
    }
    return neo_actions[agent_action]


async def print_move(agent_action: Action, neo_action: Action, agent_health: int, agent_number: int = 0):
    whitespace = " "
    null_str = ""
    print(
        f"Agent{whitespace + str(agent_number) if agent_number > 0 else null_str}: "
        f"{agent_action}, Neo: {neo_action}, Agent Health: {agent_health}"
    )


async def fight_with_one_agent(agent: Agent, agent_number: int = 0) -> None:
    agent_aiter: Agent = aiter(agent)
    while agent_aiter.health > 0:
        agent_action = await anext(agent_aiter)
        neo_action = await get_neo_action(agent_action)
        if neo_action == Action.HIGHKICK or neo_action == Action.LOWKICK:
            agent_aiter.health -= 1
        sleep: float = uniform(0.0, 0.1)
        await asyncio.sleep(sleep)
        await print_move(agent_action, neo_action, agent.health, agent_number)


async def fight() -> None:
    agent: Agent = Agent()
    await fight_with_one_agent(agent)
    print("Neo wins!")


async def fightmany(n: int) -> None:
    agents: List[Agent] = [Agent() for _ in range(n)]
    tasks: List[asyncio.Task] = [
        asyncio.create_task(fight_with_one_agent(agent, i + 1))
        for i, agent in enumerate(agents)
    ]
    shuffle(tasks)
    await asyncio.gather(*tasks, return_exceptions=True)
    print("Neo wins!")


async def main() -> None:
    print("FIGHT")
    await fight()
    print("FIGHTMANY")
    await fightmany(3)


if __name__ == '__main__':
    asyncio.run(main())
