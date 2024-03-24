import math

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    steering_angle = abs(params['steering_angle']) # Valor absoluto de ângulo de direção
    
    # Penalização por sair da pista
    if distance_from_center > 0.5 * track_width:
        return 1e-3
    
    # Calculando uma recompensa baseada na distância do carro em relação ao centro
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3
    
    # Bônus de velocidade
    if speed < 1.0:  # Limitando a velocidade para garantir que o carro se mova
        reward *= 0.5
    else:
        reward *= 1.5
    
    # Penalizando ângulos de direção excessivos
    # Ajustando para recompensar a suavidade nas curvas
    if steering_angle > 30:
        reward *= 0.8
    elif steering_angle > 15:
        reward *= 0.9
    elif steering_angle > 5:
        reward *= 0.95
    
    return float(reward)
