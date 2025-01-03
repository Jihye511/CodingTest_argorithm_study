def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while len(truck_weights) != 0:
        time += 1
        # 미리 뺴주어야함 (1초가 지날 때마다 무조건 하나는 빠지므로)
        bridge.pop(0)

        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:  # 아니면 0을 넣어줌
            bridge.append(0)


    time += bridge_length

    return time