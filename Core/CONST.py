from Core.COLOR import *

WORLD_NUMBER = 10
ZONING_NUMBER = 1

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

WORLD_WIDTH = 600
ZONING_WIDTH = 240

WORLD_SQUARE_SIZE = WORLD_WIDTH // WORLD_NUMBER
ZONING_SQUARE_SIZE = ZONING_WIDTH // ZONING_NUMBER

WORLD_POSITION_START = 0
WORLD_POSITION_END = WORLD_POSITION_START + 600

ZONING_POSITION_START_X = WORLD_WIDTH + 5
ZONING_POSITION_START_Y = WORLD_POSITION_START
ZONING_POSITION_END_X = ZONING_POSITION_START_X + ZONING_WIDTH
ZONING_POSITION_END_Y = ZONING_POSITION_START_Y + ZONING_WIDTH

WAIT_PANEL_START_X = 605
WAIT_PANEL_START_Y = 245
WAIT_PANEL_WIDTH = 243
WAIT_PANEL_HEIGHT = 355

WINDOW_TITLE = "Super Continent"
RESOURCE_PANELS = ("能量", "矿物", "食物", "物资", "合金")
RESOURCE_KEYS = ('energy', 'mineral', 'food', 'alloys', 'consumer_goods')
POWER_PANELS = ("经济", '军事', "科研")

RIGHT_ALL_PANEL_START_X = 850

RESOURCE_PANEL_START_X = RIGHT_ALL_PANEL_START_X
RESOURCE_PANEL_START_Y = 1
RESOURCE_PANEL_WIDTh = 148
RESOURCE_PANEL_HEIGHT = 135

POWER_PANEL_START_X = RIGHT_ALL_PANEL_START_X
POWER_PANEL_START_Y = 131
POWER_PANEL_WIDTH = 148
POWER_PANEL_HEIGHT = 110

RESEARCH_PANEL_START_X = RIGHT_ALL_PANEL_START_X
RESEARCH_PANEL_START_Y = 246

RESEARCH_LABEL_START_X = RESEARCH_PANEL_START_X
RESEARCH_LABEL_START_Y = RESEARCH_PANEL_START_Y
RESEARCH_LABEL_STYLE = "font: 10pt ;border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0)"

RESEARCH_RATE_BUTTON_START_X = RESEARCH_PANEL_START_X + 100
RESEARCH_RATE_BUTTON_START_Y = RESEARCH_PANEL_START_Y - 6

RESEARCH_TRANSFORM_START_X = RESEARCH_PANEL_START_X + 120
RESEARCH_TRANSFORM_START_Y = RESEARCH_PANEL_START_Y - 6

DETAIL_START_X = RIGHT_ALL_PANEL_START_X
DETAIL_START_Y = 305
DETAIL_WIDTH = 148
DETAIL_HEIGHT = 295

SPEED = 2
TIME_FLOW = 1 / SPEED

RESOURCE_WEIGHT = [(1, 5), (1, 5), (1, 5), (3, 10), (3, 10)]
INIT_RESEARCHER_RATES = (3, 3, 4)
USE_RESEARCHER_RATES = [i / 10 for i in INIT_RESEARCHER_RATES]

BLOCK_STATUS = (0, 1, 2, 3, 4)
BLOCK_WORD = ('死寂', '恶劣', '一般', '优秀', '理想')
BLOCK_STATUS_WEIGHT = (5, 23, 60, 9, 3)
BLOCK_STATUS_COLOR = (HotPink, Orange, Cyna, CornflowerBlue, SpringGreen)
BLOCK_PERCENT = (0, 25, 50, 75, 100)
BLOCK_MODIFIER = (-50, -25, 0, 25, 50)
BLOCK_ZONING_NUMBER = (3, 4, 5, 6)
