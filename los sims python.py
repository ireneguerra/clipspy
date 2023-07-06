import clips
import logging

logging.basicConfig(level=10, format='%(message)s')
env = clips.Environment()


router = clips.LoggingRouter()
env.add_router(router)

env.load('los sims.clp')
env.reset()
hours = 0
day = 0
year = 0
printon = 0

for i in range(14000):
    if hours == 24:
        hours = 0
        fact = env.assert_string('(restart)')
        env.run()
        fact.retract()
        fact = env.assert_string('(work-on)')
        env.run()
        fact.retract()
        day += 1

    if day == 10:
        print('Year: ', year)
        day = 0
        year += 1
        printon += 1
        fact = env.assert_string('(restart)')
        env.run()
        fact.retract()
        fact = env.assert_string('(increase-age)')
        env.run()
        fact.retract()
        fact = env.assert_string('(restart)')
        env.run()
        fact.retract()
        fact = env.assert_string('(now-adult)')
        env.run()
        fact.retract()
        fact = env.assert_string('(natural-death)')
        env.run()
        fact.retract()
        fact = env.assert_string('(get-partner)')
        env.run()
        fact.retract()
        act = env.assert_string('(restart)')
        env.run()
        fact.retract()
        fact = env.assert_string('(baby)')
        env.run()
        fact.retract()

    
    if printon == 9:
        fact = env.assert_string('(restart)')
        env.run()
        fact.retract()
        fact = env.assert_string('(print-all-people)')
        env.run()
        fact.retract()
        printon = 0

    if i == 0:
        fact = env.assert_string('(restart)')
        env.run()
        fact.retract()
        fact = env.assert_string('(print-all-people)')
        env.run()
        fact.retract()

    if i == 13999:
        fact = env.assert_string('(restart)')
        env.run()
        fact.retract()
        fact = env.assert_string('(print-all-people)')
        env.run()
        fact.retract()

    fact = env.assert_string('(restart)')
    env.run()
    fact.retract()
    fact = env.assert_string('(decrease-basic-needs)')
    env.run()
    fact.retract()
    fact = env.assert_string('(restart)')
    env.run()
    fact.retract()
    fact = env.assert_string('(basic-needs)')
    env.run()
    fact.retract()
    hours += 1