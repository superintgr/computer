import necessary

environment = load_environment("catalyst")
schedule = load_schedule("catalyst")

timeframes = schedule.prepare_timeframe(environment)
transforms = schedule.prepare_transforms(environment)

runner = get_runner(timeframes)
stages = set_stages(transforms)
flags = build_flags(stages)

n = 1
condition, status = flags[-n]

while condition not status:
    stage = stages[n]
    state = runner.run(stage)
    if state == status:
        n += 1
    condition, status = flags[-n]

environment = environment.integrate(stages)
schedule = schedule.integrate(environment)
message = compile_system(environment, schedule)
prinf(message)
