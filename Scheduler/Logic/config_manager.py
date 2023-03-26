def generate_elevator_configs(building_info, strategy='segmented'):
    floor_count = building_info['floor_count']
    elevator_count = building_info['elevator_count']

    if strategy == 'segmented':
        return generate_segmented_configs(floor_count, elevator_count)
    elif strategy == 'round_robin':
        return generate_round_robin_configs(floor_count, elevator_count)
    elif strategy == 'even_odd':
        return generate_even_odd_configs(floor_count, elevator_count)
    elif strategy == 'custom_ratio':
        ratios = building_info.get('ratios', [1] * elevator_count)
        return generate_custom_ratio_configs(floor_count, elevator_count, ratios)
    elif strategy == 'high_low_odd_even':
        return generate_high_low_odd_even_configs(floor_count, elevator_count)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def generate_high_low_odd_even_configs(floor_count, elevator_count):
    if elevator_count not in (4, 8, 12):
        # TODO - log this and all others
        print("ERROR: high_low_odd_even strategy requires 4, 8, or 12 elevators")
        return False

    def split_floors(floor_list, num_splits):
        split_size = len(floor_list) // num_splits
        return [floor_list[i:i + split_size] for i in range(0, len(floor_list), split_size)]

    high_floors = [floor for floor in range(1, floor_count + 1) if floor > floor_count // 2]
    low_floors = [floor for floor in range(1, floor_count + 1) if floor <= floor_count // 2]
    config_groups = [
        {'name': 'low', 'floors': low_floors},
        {'name': 'high', 'floors': high_floors},
    ]

    if elevator_count >= 8:
        config_groups.extend([
            {'name': 'lowest', 'floors': low_floors[:len(low_floors) // 2]},
            {'name': 'highest', 'floors': high_floors[len(high_floors) // 2:]},
        ])
    if elevator_count == 12:
        config_groups.extend([
            {'name': 'low_middle', 'floors': low_floors[len(low_floors) // 4:len(low_floors) // 2]},
            {'name': 'high_middle', 'floors': high_floors[:len(high_floors) // 2][len(high_floors) // 4:]},
        ])

    elevator_configs = {}
    for i, group in enumerate(config_groups):
        odd_floors = [floor for floor in group['floors'] if floor % 2 != 0]
        even_floors = [floor for floor in group['floors'] if floor % 2 == 0]
        elevator_configs[f'elevator{2 * i + 1}'] = {'accessible_floors': [1] + odd_floors}
        elevator_configs[f'elevator{2 * i + 2}'] = {'accessible_floors': [1] + even_floors}

    return elevator_configs


def generate_segmented_configs(floor_count, elevator_count):
    elevator_configs = {f'elevator{i + 1}': {'accessible_floors': [1]} for i in range(elevator_count)}

    if (floor_count - 1) / elevator_count %1 != 0:
        print('Warning: Segmented strategy requires an elevator count to be fraction of floor count-1. Rounding will occur and distribution won\'t be even')
    segment_size = (floor_count - 1) // elevator_count
    segments = [(2 + i * segment_size, 2 + (i + 1) * segment_size) for i in range(elevator_count - 1)]
    segments.append((2 + (elevator_count - 1) * segment_size, floor_count + 1))

    for i, (start, end) in enumerate(segments):
        elevator_configs[f'elevator{i + 1}']['accessible_floors'].extend(range(start, end))

    return elevator_configs


def generate_round_robin_configs(floor_count, elevator_count):
    elevator_configs = {f'elevator{i + 1}': {'accessible_floors': [1]} for i in range(elevator_count)}

    for floor in range(2, floor_count + 1):
        elevator_configs[f'elevator{(floor - 2) % elevator_count + 1}']['accessible_floors'].append(floor)

    return elevator_configs


def generate_even_odd_configs(floor_count, elevator_count):
    if elevator_count % 2 != 0:
        print("ERROR: even_odd strategy requires an even number of elevators")
        return False

    elevator_configs = {f'elevator{i + 1}': {'accessible_floors': [1]} for i in range(elevator_count)}

    odd_floors = [floor for floor in range(2, floor_count + 1) if floor % 2 != 0]
    even_floors = [floor for floor in range(2, floor_count + 1) if floor % 2 == 0]

    for i in range(elevator_count):
        if i % 2 == 0:
            elevator_configs[f'elevator{i + 1}']['accessible_floors'].extend(odd_floors)
        else:
            elevator_configs[f'elevator{i + 1}']['accessible_floors'].extend(even_floors)

    return elevator_configs


def generate_custom_ratio_configs(floor_count, elevator_count, ratios):
    if len(ratios) != elevator_count:
        raise ValueError("The length of ratios must match the elevator_count")
    ratio_sum = sum(ratios)
    if ratio_sum % (floor_count - 1) != 0:
        raise ValueError("The sum of ratios must be fraction of (the floor_count - 1)")

    elevator_configs = {f'elevator{i + 1}': {'accessible_floors': [1]} for i in range(elevator_count)}

    remaining_floors = floor_count - 1
    floor_idx = 2

    for i, ratio in enumerate(ratios):
        floors = int(remaining_floors * (ratio / ratio_sum))
        elevator_configs[f'elevator{i + 1}']['accessible_floors'].extend(range(floor_idx, floor_idx + floors))
        floor_idx += floors
        remaining_floors -= floors
        ratio_sum -= ratio

    # Distribute any remaining floors
    for floor in range(floor_idx, floor_count + 1):
        elevator_configs[f'elevator{(floor - floor_idx) % elevator_count + 1}']['accessible_floors'].append(floor)

    return elevator_configs



def generate_elevator_configs_from_scene(building_info):
    gen_config_list = []
    for strategy in ['segmented', 'round_robin', 'even_odd', 'high_low_odd_even']:
        elevator_configs = generate_elevator_configs(building_info['base'], strategy)
        if elevator_configs is False:
            continue
        if isinstance(elevator_configs, dict):
            gen_config = building_info.copy()
            gen_config['elevators'] = elevator_configs
            gen_config['base']['config_strategy'] = strategy
            gen_config_list.append(gen_config)
            #print(f"Strategy: {strategy}\nElevator Configurations:")
            #pprint(elevator_configs)
    #pprint(gen_config_list)
    return gen_config_list
