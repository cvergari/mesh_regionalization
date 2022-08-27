
from utils import generateColors


REGIONS = ['Region 1', 'Region 2', 'Region 3', 'Region 4', 'Region 5', 'Region 6']


REGION_COLORS = {}
color_values = generateColors(len(REGIONS))
for region, color in zip(REGIONS, color_values):
    REGION_COLORS[region] = color
