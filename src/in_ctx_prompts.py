DIAGRAM_PROMPT_astronomy = """Given a caption of a diagram and topic, generate the diagram layout, and then a list of required entities that would be needed to create the described diagram. Then generate a list of the relationships between the entities (i.e. which ones are connected or labeling each other). Finally, generate the location of each entity.
An entity can be an image or text. Entity locations should be generated in [x, y, width, height] format, where 0,0 is the top left corner and 100,100 is max image size.

Think step-by-step, break each caption into parts and generate the required entities, relationships, and locations for each part.

Here are some rules to follow:
All numbers should be positive, do not generate negative numbers.
Please always generate a list of entities, even if the list is empty.
Entities should not be outside the bounds [0, 0, 100, 100].
The x coordinate + the width of an entity should not exceed 100.
The y coordinate + the height of an entity should not exceed 100.
Entities of the same type should not overlap.

Here are some examples:

Caption:
A diagram showing the Earth revolving around the sun in four different phases representing each solstice or equinox.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
earth image (I0)
earth image (I1)
earth image (I2)
earth image (I3)
sun image (I4)
Entity Relationships:
I1 has an arrow to I0
I2 has an arrow to I1
I0 has an arrow to I3
I3 has an arrow to I2
Entity Locations:
I0 is located at [8, 37, 17, 28]
I1 is located at [43, 17, 14, 20]
I2 is located at [75, 37, 17, 26]
I3 is located at [40, 57, 20, 30]
I4 is located at [48, 47, 3, 6]

Caption:
A diagram showing the positions of the Earth, the Moon, and the Sun during a lunar eclipse. The Earth is directly between the sun and the moon. The moon is in the earth's shadow.
Topic:
astronomy
Diagram Layout:
abstract
Required Entities:
sun image (I0)
earth image (I1)
moon image (I2)
"Sun" text label (T0)
"Earth" text label (T1)
"Moon" text label (T2)
"Shadow" text label (T3)
Entity Relationships:
T1 labels I1
I1 is between I0 and I2
T0 labels I0
T2 labels I2
Entity Locations:
I0 is located at [8, 56, 13, 28]
I1 is located at [58, 23, 10, 18]
I2 is located at [77, 12, 4, 7]
T0 is located at [10, 86, 9, 7]
T1 is located at [46, 20, 11, 9]
T2 is located at [85, 14, 10, 9]
T3 is located at [66, 19, 12, 8]

Caption:
A diagram showing the cross section of a sun with all parts labeled. The labeled parts include eruptive prominences, coronal loops, chromosphere, sunspots, the core, radiative zone, convective zone, and the corona.
Topic:
astronomy
Diagram Layout:
abstract
Required Entities:
cross section of a sun image (I0)
sunspots image (I1)
large eruptive prominence image (I2)
coronal loops image (I3)
large eruptive prominence image (I4)
"Sunspots" text label (T0)
"Large Eruptive Prominence" text label (T1)
"Coronal Loops" text label (T2)
"Large Eruptive Prominence" text label (T3)
"Chromosphere" text label (T4)
"Solar Flares" text label (T5)
"Photosphere" text label (T6)
"Prominence" text label (T7)
"Core (Nuclear Fusion)" text label (T8)
"Radiative Zone" text label (T9)
"Convective Zone" text label (T10)
"Corona" text label (T11)
Entity Relationships:
T2 labels I3
T0 labels I1
T1 labels I2
T3 labels I5
Entity Locations:
I0 is located at [13, 14, 74, 73]
I1 is located at [37, 34, 10, 7]
I2 is located at [5, 56, 22, 26]
I3 is located at [35, 84, 8, 4]
I4 is located at [66, 71, 19, 28]
T0 is located at [37, 31, 9, 3]
T1 is located at [1, 72, 19, 5]
T2 is located at [32, 88, 14, 3]
T3 is located at [75, 82, 19, 4]
T4 is located at [36, 60, 14, 3]
T5 is located at [59, 65, 11, 3]
T6 is located at [31, 24, 12, 2]
T7 is located at [25, 13, 12, 3]
T8 is located at [49, 46, 15, 5]
T9 is located at [61, 38, 10, 5]
T10 is located at [68, 30, 12, 6]
T11 is located at [81, 21, 7, 4]

Caption:
A diagram showing the Earth going around the sun. It indicates when each equinox or solstice occurs. It also says what circle of latitude the sun is over at each point.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
"Earth + Revolution = Seasons" text label (T0)
"Vernal Equinox Sun overhead at Equator" text label (T1)
"Summer Solstice Sun overhead at Tropic of Cancer" text label (T2)
"Autumnal Equinox Sun overhead at Equator" text label (T3)
"Winter Solstice Sun overhead at Tropic of Capricorn" text label (T4)
earth image (I0)
earth image (I1)
earth image (I2)
earth image (I3)
sun image (I4)
Entity Relationships:
I4 is between I1 and I3
I1 connects to I2
T2 labels I1
I2 connects to I3
T3 labels I2
T1 labels I0
I3 connects to I0
I0 connects to I1
I4 is between I0 and I2
T4 labels I3
Entity Locations:
T0 is located at [12, 5, 71, 8]
T1 is located at [41, 17, 18, 10]
T2 is located at [1, 48, 20, 10]
T3 is located at [38, 85, 22, 9]
T4 is located at [79, 48, 18, 11]
I0 is located at [45, 28, 9, 10]
I1 is located at [21, 50, 6, 10]
I2 is located at [46, 73, 7, 11]
I3 is located at [72, 50, 7, 10]
I4 is located at [45, 50, 8, 12]

Caption:
A diagram showing the phases of the moon with the earth in the center, including the full moon, new moon, first quarter, last quarter, and the crescent and gibbous phases. The sun is included on the side of the new moon.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
moon image (I0)
moon image (I1)
moon image (I2)
moon image (I3)
moon image (I4)
moon image (I5)
moon image (I6)
moon image (I7)
sun image (I8)
"Waning Crescent" text label (T0)
"Last Quarter" text label (T1)
"Waning Gibbous" text label (T2)
"Full Moon" text label (T3)
"Waxing GIbbous" text label (T4)
"First Quarter" text label (T5)
"Waxing Crescent" text label (T6)
"New Moon" text label (T7)
Entity Relationships:
T0 labels I7
I8 left I5
T7 labels I6
I8 left I4
I8 left I2
T2 labels I1
I8 left I1
T3 labels I2
T1 labels I0
T5 labels I4
I8 left I0
I8 left I7
T6 labels I5
I8 left I3
I8 left I6
T4 labels I3
Entity Locations:
I0 is located at [47, 14, 12, 15]
I1 is located at [68, 21, 11, 16]
I2 is located at [79, 42, 12, 15]
I3 is located at [68, 66, 12, 15]
I4 is located at [47, 71, 12, 15]
I5 is located at [27, 66, 12, 14]
I6 is located at [16, 42, 11, 15]
I7 is located at [27, 21, 12, 15]
I8 is located at [0, 0, 9, 100]
T0 is located at [18, 10, 11, 7]
T1 is located at [45, 8, 15, 4]
T2 is located at [77, 10, 9, 8]
T3 is located at [86, 31, 12, 4]
T4 is located at [83, 68, 10, 8]
T5 is located at [45, 88, 15, 4]
T6 is located at [14, 69, 12, 6]
T7 is located at [9, 31, 13, 5]

Caption:
A diagram showing the Perigee and Apogee phases of the moon as it orbits around Earth.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
moon image (I0)
moon image (I1)
"Moon" text label (T0)
"Earth" text label (T1)
earth image (I2)
"Moon's Orbit" text label (T2)
"Apogee" text label (T3)
"Pergiee" text label (T4)
Entity Relationships:
T0 labels I1
T4 labels I0
T0 labels I0
T3 labels I1
T1 labels I2
I2 is between I0 and I1
I1 has an arrow to I0
I0 has an arrow to I1
Entity Locations:
I0 is located at [4, 40, 8, 14]
I1 is located at [87, 38, 9, 16]
T0 is located at [80, 29, 15, 8]
T1 is located at [29, 61, 16, 7]
I2 is located at [29, 32, 16, 27]
T2 is located at [57, 80, 25, 16]
T3 is located at [74, 51, 14, 9]
T4 is located at [12, 36, 14, 8]

Caption:
A diagram showing the Earth revolving around the sun at four points.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
earth image (I0)
earth image (I1)
earth image (I2)
earth image (I3)
sun image (I4)
"Sun" text label (T0)
Entity Relationships:
T0 labels I4
I4 is between I1 and I3
I4 is between I0 and I2
Entity Locations:
I0 is located at [44, 18, 9, 11]
I1 is located at [65, 42, 9, 12]
I2 is located at [44, 68, 9, 12]
I3 is located at [22, 44, 10, 11]
I4 is located at [41, 38, 17, 21]
T0 is located at [45, 45, 7, 5]

Caption:
A diagram showing the Earth revolving around the sun. The solstices and equinoxes are labeled at each Earth phase in the rotation. There are also labels indicating which hemispheres get the most solar energy at each Earth phase.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
earth image (I0)
earth image (I1)
earth image (I2)
earth image (I3)
"Vernal Equinox March 21-22 Incoming solar energy equal in both hemispheres" text label (T0)
"Summer Solstice June 21-22 Incoming solar energy greatest in Northern Hemisphere" text label (T1)
"Autumnal Equinox September 22-23 Incoming solar energy equal in both hemispheres" text label (T2)
"Winter Solstice December 21-22 Incoming solar energy greatest in Southern Hemisphere" text label (T3)
"Orbit" text label (T4)
"Sun" text label (T5)
earth image (I4)
Entity Relationships:
I1 has an arrow to I2
I4 is between I1 and I3
T3 labels I3
I3 has an arrow to I0
T0 labels I0
T2 labels I2
T5 labels I4
T1 labels I1
I4 is between I0 and I2
I0 has an arrow to I1
I2 has an arrow to I3
Entity Locations:
I0 is located at [39, 11, 17, 21]
I1 is located at [3, 41, 18, 21]
I2 is located at [38, 74, 18, 22]
I3 is located at [78, 41, 17, 20]
T0 is located at [57, 1, 22, 22]
T1 is located at [0, 65, 19, 25]
T2 is located at [58, 82, 29, 18]
T3 is located at [80, 65, 19, 24]
T4 is located at [24, 71, 7, 3]
T5 is located at [45, 50, 6, 3]
I4 is located at [40, 42, 16, 18]

Caption:
A diagram showing the relative the Sun, Moon, and Earth during a total lunar eclipse. It also has the umbra and penumbra labels.
Topic:
astronomy
Diagram Layout:
rows
Required Entities:
"Sun" text label (T0)
"Earth" text label (T1)
"Moon" text label (T2)
"Total Lunar Eclipse" text label (T3)
"Umbra" text label (T4)
"Penumbra" text label (T5)
sun image (I0)
earth image (I1)
moon image (I2)
Entity Relationships:
T0 labels I0
I1 is between I0 and I2
T2 labels I2
T1 label I1
Entity Locations:
T0 is located at [13, 92, 4, 6]
T1 is located at [66, 91, 6, 6]
T2 is located at [79, 92, 7, 7]
T3 is located at [40, 3, 19, 7]
T4 is located at [70, 10, 7, 6]
T5 is located at [88, 25, 11, 7]
I0 is located at [1, 14, 29, 69]
I1 is located at [64, 38, 9, 22]
I2 is located at [80, 44, 4, 10]

Caption:
A diagram showing the alignment of the Sun, the Moon, and the Earth at various points through out the moon's rotation around Earth.
Topic:
astronomy
Diagram Layout:
tree
Required Entities:
sun image (I0)
earth image (I1)
moon image (I2)
earth image (I3)
moon image (I4)
earth image (I5)
moon image (I6)
earth image (I7)
moon image (I8)
"Similarly, the alignment of the Sun, Moon, and Earth during a new moon results in spring tides." text label (T0)
"New moon" text label (T1)
"Gravitational pull of Sun and Moon" text label (T2)
"Spring tide" text label (T3)
Entity Relationships:
I5 has an arrow to I0
I0 left I1
I0 has an arrow to I5
I0 has an arrow to I3
I8 below I7
I3 has an arrow to I0
I0 has an arrow to I7
I0 left I7
I0 left I3
I2 left I1
I6 right I5
I4 above I3
I1 has an arrow to I0
I0 has an arrow to I1
I7 has an arrow to I0
I0 left I5
Entity Locations:
I0 is located at [16, 11, 25, 62]
I1 is located at [72, 3, 13, 14]
I2 is located at [69, 11, 4, 7]
I3 is located at [78, 22, 11, 20]
I4 is located at [78, 17, 6, 5]
I5 is located at [77, 45, 14, 13]
I6 is located at [91, 50, 4, 7]
I7 is located at [75, 61, 11, 16]
I8 is located at [75, 79, 6, 5]
T0 is located at [5, 86, 92, 12]
T1 is located at [57, 26, 12, 5]
T2 is located at [16, 4, 17, 5]
T3 is located at [34, 14, 18, 7]

Caption:
"""

AUDITOR_PROMPT_astronomy = """Given a caption and a layout of a diagram, you should determine if something is wrong in the diagram based on the caption. You should explain your answer. Think step-by-step as to why the diagram is correct or not.
The diagram will be described in terms of entities in the diagram, the relationships between the entities, and the location of each entity.
An entity can be an image or text. Entity locations will be in [x, y, width, height] format, where 0,0 is the top left corner and 100,100 is max image size.

Here are some rules the diagrams should follow:
All numbers should be positive, no negative numbers.
Entities should not be outside the bounds [0, 0, 100, 100].
The x coordinate + the width of an entity should not exceed 100.
The y coordinate + the height of an entity should not exceed 100.
Entities of the same type should not overlap.

Here are some examples:
Caption:
A diagram showing where the tides occur on Earth and the angle to the moon. This angle is indicated by the declination of Moon.
Topic:
astronomy
Diagram Layout:
abstract
Required Entities:
earth image (I0)
moon image (I1)
"High Tide" text label (T0)
"Low Tide" text label (T1)
"Declination of Moon" text label (T2)
"Angle" text label (T3)
Entity Relationships:
T3 labels I0 and I1
T1 labels I0
T0 labels I0
T2 labels I1
Entity Locations:
I0 is located at [20, 30, 30, 40]
I1 is located at [70, 30, 20, 20]
T0 is located at [10, 20, 10, 5]
T1 is located at [10, 75, 10, 5]
T2 is located at [70, 10, 20, 5]
T3 is located at [50, 50, 10, 5]
What is wrong with this diagram?
The declination of the moon text should be inbetween the moon and the earth. The high tide text should be on the side of earth that is facing the moon and low tide should be on the other side. The tidal bulge location should also be marked.

Caption:
A diagram showing the phases of the moon as it revolves around Earth, including the first quarter, waxing crescent, waning crescent, full moon, new moon, wanning crescent, and waxing crescent. It also indicates where the sunlight is coming from.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
moon image (I0)
moon image (I1)
moon image (I2)
moon image (I3)
moon image (I4)
moon image (I5)
moon image (I6)
moon image (I7)
"First Quarter" text label (T0)
"Waxing Crescent" text label (T1)
"Waning Crescent" text label (T2)
"Full Moon" text label (T3)
"New Moon" text label (T4)
"Waning Crescent" text label (T5)
"Waxing Crescent" text label (T6)
"Sunlight" text label (T7)
Entity Relationships:
T5 labels I5
T6 labels I6
T2 labels I2
T7 points to I7
T1 labels I1
T3 labels I3
T4 labels I4
T0 labels I0
Entity Locations:
I0 is located at [20, 50, 10, 15]
I1 is located at [35, 30, 10, 15]
I2 is located at [50, 20, 10, 15]
I3 is located at [65, 30, 10, 15]
I4 is located at [80, 50, 10, 15]
I5 is located at [65, 70, 10, 15]
I6 is located at [50, 80, 10, 15]
I7 is located at [35, 70, 10, 15]
T0 is located at [15, 45, 15, 5]
T1 is located at [30, 25, 15, 5]
T2 is located at [45, 15, 15, 5]
T3 is located at [60, 25, 15, 5]
T4 is located at [75, 45, 15, 5]
T5 is located at [60, 65, 15, 5]
T6 is located at [45, 85, 15, 5]
T7 is located at [30, 65, 15, 5]
What is wrong with this diagram?
There should be an earth in the center of the moons. The moon phases are out of order, it should go from new moon to waxing crescent to first quarter to waxing gibbous to full moon to waning gibbous to last quarter to waning crescent. The sunlight label should be to the side of the diagram where the new moon is.

Caption:
A diagram showing the phases of the moon as it revolves around the Earth, including the full moon, new moon, first quarter, last quarter, waxing crescent, waning crescent, waxing gibbous, and waning gibbous. It also indicates which day of the month each moon phase occurs.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
moon image (I0)
moon image (I1)
moon image (I2)
moon image (I3)
moon image (I4)
moon image (I5)
moon image (I6)
moon image (I7)
earth image (I8)
"Full Moon (Day 15)" text label (T0)
"New Moon (Day 1)" text label (T1)
"First Quarter (Day 7)" text label (T2)
"Last Quarter (Day 22)" text label (T3)
"Waxing Crescent (Day 3)" text label (T4)
"Waning Crescent (Day 27)" text label (T5)
"Waxing Gibbous (Day 11)" text label (T6)
"Waning Gibbous (Day 18)" text label (T7)
Entity Relationships:
T5 labels I5
T6 labels I6
T2 labels I2
T7 labels I7
T1 labels I1
T3 labels I3
T4 labels I4
T0 labels I0
Entity Locations:
I0 is located at [50, 50, 10, 10]
I1 is located at [75, 50, 10, 10]
I2 is located at [50, 75, 10, 10]
I3 is located at [25, 50, 10, 10]
I4 is located at [65, 65, 10, 10]
I5 is located at [35, 35, 10, 10]
I6 is located at [65, 35, 10, 10]
I7 is located at [35, 65, 10, 10]
I8 is located at [50, 50, 20, 20]
T0 is located at [52, 52, 15, 5]
T1 is located at [77, 52, 15, 5]
T2 is located at [52, 77, 15, 5]
T3 is located at [27, 52, 15, 5]
T4 is located at [67, 67, 15, 5]
T5 is located at [37, 37, 15, 5]
T6 is located at [67, 37, 15, 5]
T7 is located at [37, 67, 15, 5]
What is wrong with this diagram?
The moon phases are out of order, it should go from new moon to waxing crescent to first quarter to waxing gibbous to full moon to waning gibbous to last quarter to waning crescent. The text labels should be further away from their images so there do not overlap. The only object in the center should be an image of the earth, there should not be any moons in the center.

Caption:
A diagram showing the rotation axis of the Earth, marking the positions of the North Pole and the South Pole. It indicates where on earth long days, short days, equal days occur if the sunlight is coming in from the side. It also indicates where on earth the sun never sets and where the sun never rises.
Topic:
astronomy
Diagram Layout:
abstract
Required Entities:
earth image (I0)
"North Pole" text label (T1)
"South Pole" text label (T2)
"Long Days" text label (T3)
"Short Days" text label (T4)
"Equal Days" text label (T5)
"Sun Never Sets" text label (T6)
"Sun Never Rises" text label (T7)
"Sunlight" text label (T8)
"Rotation Axis" text label (T9)
Entity Relationships:
T3 labels I0
T9 labels I0
T4 labels I0
T6 labels I0
T7 labels I0
T1 labels I0
T5 labels I0
T2 labels I0
T8 labels I0
Entity Locations:
I0 is located at [30, 20, 40, 60]
T1 is located at [35, 10, 10, 5]
T2 is located at [35, 80, 10, 5]
T3 is located at [10, 30, 10, 5]
T4 is located at [80, 30, 10, 5]
T5 is located at [45, 10, 10, 5]
T6 is located at [10, 60, 10, 5]
T7 is located at [80, 60, 10, 5]
T8 is located at [45, 80, 10, 5]
T9 is located at [30, 50, 10, 5]
What is wrong with this diagram?
The sunlight should either be on the right or left side of the diagram, not in the bottom. Short days and longs should be on the same left or right side, but opposite top and bottom sides.

Caption:
A diagram showing all eight planets in the solar system in order, starting with Mercury and ending with Neptune. It also indicates the axial tilt of each planet.
Topic:
astronomy
Diagram Layout:
linear
Required Entities:
"Mercury" text label (T0)
"Venus" text label (T1)
"Earth" text label (T2)
"Mars" text label (T3)
"Jupiter" text label (T4)
"Saturn" text label (T5)
"Uranus" text label (T6)
"Neptune" text label (T7)
mercury image (I0)
venus image (I1)
earth image (I2)
mars image (I3)
jupiter image (I4)
saturn image (I5)
uranus image (I6)
neptune image (I7)
"axial tilt" text label (T8)
Entity Relationships:
T5 labels I5
T6 labels I6
T2 labels I2
T7 labels I7
T1 labels I1
T3 labels I3
T4 labels I4
T0 labels I0
Entity Locations:
T0 is located at [5, 5, 10, 5]
T1 is located at [20, 5, 10, 5]
T2 is located at [35, 5, 10, 5]
T3 is located at [50, 5, 10, 5]
T4 is located at [65, 5, 10, 5]
T5 is located at [80, 5, 10, 5]
T6 is located at [95, 5, 10, 5]
T7 is located at [110, 5, 10, 5]
I0 is located at [5, 15, 10, 10]
I1 is located at [20, 15, 10, 10]
I2 is located at [35, 15, 10, 10]
I3 is located at [50, 15, 10, 10]
I4 is located at [65, 15, 10, 10]
I5 is located at [80, 15, 10, 10]
I6 is located at [95, 15, 10, 10]
I7 is located at [110, 15, 10, 10]
T8 is located at [60, 30, 20, 5]
What is wrong with this diagram?
The axial tilt of each planet should be shown in the diagram. For example, mercury has an axial tilt of 0.01 and neptune has an axial tilt of 28.32.

Caption:
A diagram showing the four phases of the moon side by side along with the dates in January when each phase occurs. It shows waxing crescent, waxing gibbous, new moon, and full moon.
Topic:
astronomy
Diagram Layout:
rows
Required Entities:
moon image (I0)
moon image (I1)
moon image (I2)
moon image (I3)
moon image (I4)
moon image (I5)
moon image (I6)
moon image (I7)
"New Moon January 1" text label (T0)
"Waxing Crescent January 5" text label (T1)
"First Quarter January 9" text label (T2)
"Waxing Gibbous January 13" text label (T3)
"Full Moon January 17" text label (T4)
"Waning Gibbous January 21" text label (T5)
"Last Quarter January 25" text label (T6)
"Waning Crescent January 29" text label (T7)
Entity Relationships:
T5 labels I5
T6 labels I6
T2 labels I2
T7 labels I7
T1 labels I1
T3 labels I3
T4 labels I4
T0 labels I0
Entity Locations:
I0 is located at [1, 10, 12, 20]
I1 is located at [15, 10, 12, 20]
I2 is located at [29, 10, 12, 20]
I3 is located at [43, 10, 12, 20]
I4 is located at [57, 10, 12, 20]
I5 is located at [71, 10, 12, 20]
I6 is located at [85, 10, 12, 20]
I7 is located at [99, 10, 12, 20]
T0 is located at [1, 32, 12, 5]
T1 is located at [15, 32, 18, 5]
T2 is located at [29, 32, 16, 5]
T3 is located at [43, 32, 18, 5]
T4 is located at [57, 32, 12, 5]
T5 is located at [71, 32, 18, 5]
T6 is located at [85, 32, 14, 5]
T7 is located at [99, 32, 18, 5]
What is wrong with this diagram?
The order of the moons should be waxing crescent, waxing gibbous, then new moon, and then full moon. Other moon phases should be skipped.

Caption:
A diagram showing the phases of the moon as it revolves around Earth, including waxing, full, waning, and quarter moons. It also has the sun on the side of the diagram to indicate where the light is coming from.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
moon image (I0)
moon image (I1)
moon image (I2)
moon image (I3)
moon image (I4)
moon image (I5)
moon image (I6)
moon image (I7)
sun image (I8)
"Waxing Crescent" text label (T0)
"First Quarter" text label (T1)
"Waxing Gibbous" text label (T2)
"Full Moon" text label (T3)
"Waning Gibbous" text label (T4)
"Last Quarter" text label (T5)
"Waning Crescent" text label (T6)
"New Moon" text label (T7)
Entity Relationships:
T5 labels I4
T3 labels I2
T0 labels I7
T2 labels I1
T1 labels I0
T6 labels I5
T4 labels I3
T7 labels I6
Entity Locations:
I0 is located at [47, 14, 12, 15]
I1 is located at [68, 21, 11, 16]
I2 is located at [79, 42, 12, 15]
I3 is located at [68, 66, 12, 15]
I4 is located at [47, 71, 12, 15]
I5 is located at [27, 66, 12, 14]
I6 is located at [16, 42, 11, 15]
I7 is located at [27, 21, 12, 15]
I8 is located at [0, 0, 9, 100]
T0 is located at [18, 10, 11, 7]
T1 is located at [45, 8, 15, 4]
T2 is located at [77, 10, 9, 8]
T3 is located at [86, 31, 12, 4]
T4 is located at [83, 68, 10, 8]
T5 is located at [45, 88, 15, 4]
T6 is located at [14, 69, 12, 6]
T7 is located at [9, 31, 13, 5]
What is wrong with this diagram?
There should be an earth in the center of the moons. There should also be a sun on the side of the diagram where the new moon is, to indicated where the sunlight is coming from.

Caption:
A diagram showing the positions of the Earth as it orbits the sun during different seasons. It also indicates if there is an equinox or solstice at each point and which day in the year it occurs.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
earth image (I0)
earth image (I1)
earth image (I2)
earth image (I3)
sun image (I4)
"Vernal Equinox March 20" text label (T0)
"Summer Solstice June 21" text label (T1)
"Autumnal Equinox September 22" text label (T2)
"Winter Solstice December 21" text label (T3)
Entity Relationships:
T2 labels I2
I4 is between I0 and I2
T1 labels I1
T3 labels I3
T0 labels I0
I4 is between I1 and I3
Entity Locations:
I0 is located at [45, 18, 9, 11]
I1 is located at [65, 42, 9, 12]
I2 is located at [44, 68, 9, 12]
I3 is located at [22, 44, 10, 11]
I4 is located at [41, 38, 17, 21]
T0 is located at [45, 10, 15, 5]
T1 is located at [70, 40, 15, 5]
T2 is located at [45, 80, 20, 5]
T3 is located at [15, 40, 15, 5]
What is wrong with this diagram?
The text should be placed a little further away from the images they label so there is no overlap. The text labels should also be slightly larger. The earth images should also have arrows pointing between them in the order of the months.

Caption:
A diagram showing the seasons as the Earth orbits around the Sun. It illustrates the different seasons in each hemisphere at each equinox and solstice.
Topic:
astronomy
Diagram Layout:
circular
Required Entities:
earth image (I0)
earth image (I1)
earth image (I2)
earth image (I3)
sun image (I4)
"Spring Equinox" text label (T0)
"Summer Solstice" text label (T1)
"Autumn Equinox" text label (T2)
"Winter Solstice" text label (T3)
"Northern Hemisphere" text label (T4)
"Southern Hemisphere" text label (T5)
Entity Relationships:
I1 has an arrow to I0
I3 has an arrow to I2
I0 has an arrow to I3
T2 labels I2
T5 labels I2 and I3
I2 has an arrow to I1
T1 labels I1
T3 labels I3
T4 labels I0 and I1
T0 labels I0
Entity Locations:
I0 is located at [8, 37, 17, 28]
I1 is located at [43, 17, 14, 20]
I2 is located at [75, 37, 17, 26]
I3 is located at [40, 57, 20, 30]
I4 is located at [48, 47, 3, 6]
T0 is located at [8, 30, 17, 7]
T1 is located at [43, 10, 14, 7]
T2 is located at [75, 30, 17, 7]
T3 is located at [40, 50, 20, 7]
T4 is located at [25, 5, 20, 7]
T5 is located at [25, 88, 20, 7]
What is wrong with this diagram?
The earths should be the same size. The sun should be a little bigger. The seasons should be labled in each hemisphere for each earth image. For example, in the bottom earth that covers winter solstice, it should say northern winter and southern summer to indicate the season in each hemisphere.

"""

DIAGRAM_PROMPT_biology = """Given a caption of a diagram and topic, generate the diagram layout, and then a list of required entities that would be needed to create the described diagram. Then generate a list of the relationships between the entities (i.e. which ones are connected or labeling each other). Finally, generate the location of each entity.
An entity can be an image or text. Entity locations should be generated in [x, y, width, height] format, where 0,0 is the top left corner and 100,100 is max image size.

Think step-by-step, break each caption into parts and generate the required entities, relationships, and locations for each part.

Here are some rules to follow:
All numbers should be positive, do not generate negative numbers.
Please always generate a list of entities, even if the list is empty.
Entities should not be outside the bounds [0, 0, 100, 100].
The x coordinate + the width of an entity should not exceed 100.
The y coordinate + the height of an entity should not exceed 100.
Entities of the same type should not overlap.

Here are some examples:

Caption:
A diagram showing a food chain, illustrating the relationships among various animals and their connections to each other through feeding habits. It includes dragonfly, frog, snake, buzzard, fox, ladybird, butterfly, greenfly, titmouse, mouse, rabbit, plantain, grasshopper, and berries.
Topic:
biology
Diagram Layout:
tree
Required Entities:
dragonfly image (I0)
buzzard image (I1)
fox image (I2)
frog image (I3)
snake image (I4)
ladybird image (I5)
mouse image (I6)
titmouse image (I7)
greenfly image (I8)
butterfly image (I9)
rabbit image (I10)
grasshopper image (I11)
berries image (I12)
plantain image (I13)
"dragonfly" text label (T0)
"buzzard" text label (T1)
"fox" text label (T2)
"frog" text label (T3)
"snake" text label (T4)
"ladybird" text label (T5)
"mouse" text label (T6)
"titmouse" text label (T7)
"greenfly" text label (T8)
"butterfly" text label (T9)
"rabbit" text label (T10)
"grasshopper" text label (T11)
"berries" text label (T12)
"plantain" text label (T13)
Entity Relationships:
T13 labels I13
I13 has an arrow to I11
I3 has an arrow to I4
T0 labels I0
I4 has an arrow to I1
T1 labels I1
T2 labels I2
I6 has an arrow to I1
T5 labels I5
T12 labels I12
I7 has an arrow to I4
I13 has an arrow to I10
I11 has an arrow to I3
I7 has an arrow to I2
I12 has an arrow to I7
T6 labels I6
T11 labels I11
I12 has an arrow to I8
I5 has an arrow to I0
T9 labels I9
I10 has an arrow to I2
I6 has an arrow to I2
T4 labels I4
T7 labels I7
I12 has an arrow to I11
I5 has an arrow to I7
I7 has an arrow to I1
T10 labels I10
I9 has an arrow to I3
I13 has an arrow to I6
I8 has an arrow to I5
T8 labels I8
I10 has an arrow to I1
I12 has an arrow to I9
I0 has an arrow to I3
T3 labels I3
Entity Locations:
I0 is located at [9, 7, 13, 10]
I1 is located at [60, 0, 10, 19]
I2 is located at [75, 5, 24, 15]
I3 is located at [24, 20, 13, 12]
I4 is located at [43, 27, 12, 13]
I5 is located at [9, 35, 10, 9]
I6 is located at [67, 39, 13, 16]
I7 is located at [45, 46, 14, 11]
I8 is located at [7, 56, 12, 9]
I9 is located at [24, 53, 17, 10]
I10 is located at [83, 48, 13, 14]
I11 is located at [35, 69, 12, 8]
I12 is located at [9, 84, 16, 11]
I13 is located at [59, 75, 11, 21]
T0 is located at [8, 2, 13, 6]
T1 is located at [50, 2, 11, 5]
T2 is located at [85, 2, 9, 3]
T3 is located at [29, 16, 8, 4]
T4 is located at [42, 23, 9, 4]
T5 is located at [0, 30, 12, 6]
T6 is located at [60, 47, 9, 4]
T7 is located at [46, 58, 14, 5]
T8 is located at [1, 64, 12, 5]
T9 is located at [17, 50, 11, 4]
T10 is located at [88, 61, 9, 4]
T11 is located at [32, 78, 17, 5]
T12 is located at [12, 96, 11, 4]
T13 is located at [69, 92, 11, 4]

Caption:
A diagram showing the life cycle of a butterfly, going from the stage of an egg, to a caterpillar, to a cocoon, to an adult butterfly.
Topic:
biology
Diagram Layout:
circular
Required Entities:
adult butterfly image (I0)
egg image (I1)
caterpillar image (I2)
chrysalis image (I3)
"adult" text label (T0)
"egg" text label (T1)
"caterpillar" text label (T2)
"chrysalis" text label (T3)
Entity Relationships:
T2 labels I2
T1 labels I1
T0 labels I0
T3 labels I3
Entity Locations:
I0 is located at [43, 5, 22, 30]
I1 is located at [72, 54, 9, 6]
I2 is located at [50, 82, 26, 8]
I3 is located at [24, 46, 10, 29]
T0 is located at [68, 16, 18, 9]
T1 is located at [82, 54, 12, 6]
T2 is located at [52, 91, 22, 7]
T3 is located at [3, 77, 31, 9]

Caption:
A diagram showing the cycle of a Take-all Gaeumannomyces graminis infection a plant. It first causes a severe infection which results in stunted patches and a rat tail appearance of roots and whiteheads. Then it overwinters as mycelium on roots and stem bases of infected plants. Then it makes a runner hyphase on roots. Then the cycle repeats.
Topic:
biology
Diagram Layout:
circular
Required Entities:
"take-all gaeumannomyces graminis" text label (T0)
"severe infection results in stunted patches, 'rat tail' appearance of roots and whiteheads" text label (T1)
"whitehead" text label (T2)
"fungus overwinters as mycelium on roots and stem bases of infected plants, spreading to volunteers and autumn sown crops." text label (T3)
"runner hyphae on roots" text label (T4)
plant with roots image (I0)
roots image (I1)
roots image (I2)
whitehead plant image (I3)
Entity Relationships:
T3 has an arrow to I2
I1 has an arrow to I0
T1 has an arrow to T3
T2 labels I3
I0 has an arrow to T1
T3 has an arrow to I1
T4 labels I1
Entity Locations:
T0 is located at [20, 0, 52, 13]
T1 is located at [39, 19, 61, 10]
T2 is located at [81, 66, 15, 6]
T3 is located at [39, 81, 61, 16]
T4 is located at [0, 87, 33, 5]
I0 is located at [9, 28, 16, 31]
I1 is located at [4, 60, 13, 25]
I2 is located at [48, 45, 14, 26]
I3 is located at [87, 33, 6, 30]

Caption:
A diagram showing the life cycle of a cockroach, illustrating the different stages from egg to nymphs to adult.
Topic:
biology
Diagram Layout:
circular
Required Entities:
adult bug image (I0)
egg image (I1)
nymph bug image (I2)
nymph bug image (I3)
"adult 10-20 days" text label (T0)
"egg 1-8 days" text label (T1)
"nymphs 14 days" text label (T2)
Entity Relationships:
T0 labels I0
I2 has an arrow to I3
T2 labels I2
I0 has an arrow to I1
I3 has an arrow to I0
T2 labels I3
T1 labels I1
I1 has an arrow to I2
Entity Locations:
I0 is located at [35, 0, 40, 41]
I1 is located at [94, 54, 6, 14]
I2 is located at [46, 80, 20, 20]
I3 is located at [0, 44, 28, 28]
T0 is located at [49, 51, 14, 11]
T1 is located at [84, 57, 9, 11]
T2 is located at [29, 71, 20, 9]

Caption:
A diagram showing the life cycle of a grasshopper, including the wingless nymph, eggs in ground, and winged adult stages.
Topic:
biology
Diagram Layout:
circular
Required Entities:
"wingless nymph" text label (T0)
"winged adult" text label (T1)
"eggs in ground" text label (T2)
"grasshopper lifecycle" text label (T3)
nymph grasshopper image (I0)
adult grasshopper image (I1)
egg image (I2)
Entity Relationships:
T2 labels I2
T1 labels I1
T0 labels I0
Entity Locations:
T0 is located at [45, 3, 20, 9]
T1 is located at [74, 73, 26, 8]
T2 is located at [0, 43, 15, 13]
T3 is located at [22, 92, 49, 8]
I0 is located at [32, 13, 38, 26]
I1 is located at [29, 51, 45, 37]
I2 is located at [16, 39, 12, 20]

Caption:
A diagram showing a sweetpotato whitefly, greenhouse whitefly, and a bandedwing whitefly.
Topic:
biology
Diagram Layout:
rows
Required Entities:
"sweetpotato whitefly" text label (T0)
"greenhouse whitefly" text label (T1)
"bandedwing whitefly" text label (T2)
fly image (I0)
fly image (I1)
fly image (I2)
Entity Relationships:
T2 labels I2
T1 labels I1
T0 labels I0
Entity Locations:
T0 is located at [13, 69, 23, 11]
T1 is located at [38, 69, 22, 11]
T2 is located at [64, 69, 21, 11]
I0 is located at [17, 18, 20, 48]
I1 is located at [37, 17, 22, 50]
I2 is located at [60, 17, 24, 49]

Caption:
A diagram showing the Ladybug Life Cycle from an egg, to a larva, to a pupa, and then an adult.
Topic:
biology
Diagram Layout:
circular
Required Entities:
egg image (I0)
larva image (I1)
pupa image (I2)
adult ladybug image (I3)
"egg" text label (T0)
"larva" text label (T1)
"pupa" text label (T2)
"adult" text label (T3)
"ladybug life cycle" text label (T4)
Entity Relationships:
T2 labels I2
T1 labels I1
T0 labels I0
T3 labels I3
Entity Locations:
I0 is located at [46, 23, 6, 6]
I1 is located at [71, 39, 16, 20]
I2 is located at [39, 67, 24, 11]
I3 is located at [8, 37, 26, 25]
T0 is located at [43, 31, 10, 4]
T1 is located at [59, 44, 14, 4]
T2 is located at [44, 63, 15, 4]
T3 is located at [34, 46, 13, 4]
T4 is located at [23, 4, 52, 6]

Caption:
A diagram showing the food web, which is a series of interconnected relationships between various animals and plants. The web includes, grass, two different plants, a grasshopper, a mouse, a butterfly, a hawk, a snake, a deer, and a wolf.
Topic:
biology
Diagram Layout:
tree
Required Entities:
"food web" text label (T0)
wolf image (I0)
deer image (I1)
snake image (I2)
mouse image (I3)
bird image (I4)
grasshopper image (I5)
butterfly image (I6)
grass image (I7)
plant image (I8)
plant image (I9)
Entity Relationships:
I5 connects to I8
I6 connects to I9
I0 connects to I1
I1 connects to I7
I3 connects to I7
I2 connects to I3
I3 connects to I9
I2 connects to I5
I3 connects to I4
I0 connects to I3
I5 connects to I7
I3 connects to I8
Entity Locations:
T0 is located at [60, 10, 16, 5]
I0 is located at [31, 2, 22, 26]
I1 is located at [1, 13, 19, 39]
I2 is located at [22, 30, 21, 15]
I3 is located at [35, 44, 21, 14]
I4 is located at [61, 23, 18, 18]
I5 is located at [14, 56, 20, 12]
I6 is located at [79, 41, 20, 19]
I7 is located at [7, 74, 23, 23]
I8 is located at [42, 67, 15, 29]
I9 is located at [66, 59, 12, 33]

Caption:
A diagram showing the relationships between different organisms in a food chain. It includes, kingfisher, fish, water flea, algae, water boatman, and dragonfly nymph.
Topic:
biology
Diagram Layout:
tree
Required Entities:
"Kingfisher" text label (T0)
"Fish" text label (T1)
"Water flea" text label (T2)
"Algae" text label (T3)
"Water boatman" text label (T4)
"Dragonfly nymph" text label (T5)
Entity Relationships:
T1 has an arrow to T5
T3 has an arrow to T1
T1 has an arrow to T0
T2 has an arrow to T4
T3 has an arrow to T2
T3 has an arrow to T4
T2 has an arrow to T1
T4 has an arrow to T5
Entity Locations:
T0 is located at [16, 3, 22, 6]
T1 is located at [8, 27, 10, 6]
T2 is located at [50, 26, 23, 6]
T3 is located at [32, 51, 14, 7]
T4 is located at [74, 50, 16, 8]
T5 is located at [51, 88, 19, 9]

Caption:
A diagram showing the food web of Onondaga Lake, which includes fish eating animals, plants and algae, macroinvertebrates, juveniles, planktivores, and zooplankton. It also indicates how other environmental factors affect the web.
Topic:
biology
Diagram Layout:
tree
Required Entities:
fish-eating animals image (I0)
game fish image (I1)
plants and algae image (I2)
juvenile fish image (I3)
macroinvertebrates image (I4)
planktivores image (I5)
zooplankton image (I6)
"fish-eating animals" text label (T0)
"game fish" text label (T1)
"plants and algae" text label (T2)
"macroinvertebrates (insects, worms, and snails that live in the bottom sediments)" text label (T3)
"juveniles" text label (T4)
"planktivores (fish that eat plankton)" text label (T5)
"zooplankton" text label (T6)
"nutrients (such as phosphorus and nitrogen)" text label (T7)
"sources: urban & rural runoff" text label (T8)
"sunlight" text label (T9)
"carbon dioxide (c02)" text label (T10)
"onondaga lake food web" text label (T11)
Entity Relationships:
T0 labels I0
I6 has an arrow to I5
T6 labels I6
T8 has an arrow to T7
T1 labels I1
T3 labels I3
I3 has an arrow to I1
T5 labels I5
I2 has an arrow to I3
T2 labels I2
I2 has an arrow to I5
I4 has an arrow to I1
I2 has an arrow to I6
I6 has an arrow to I4
T4 labels I4
I3 has an arrow to I4
T7 has an arrow to I2
I1 has an arrow to I0
T10 has an arrow to I2
T9 has an arrow to I2
Entity Locations:
I0 is located at [1, 11, 21, 12]
I1 is located at [2, 35, 31, 14]
I2 is located at [38, 31, 23, 14]
I3 is located at [23, 59, 18, 9]
I4 is located at [13, 72, 12, 17]
I5 is located at [47, 58, 11, 17]
I6 is located at [65, 55, 9, 15]
T0 is located at [22, 14, 14, 4]
T1 is located at [15, 50, 8, 4]
T2 is located at [41, 46, 13, 3]
T3 is located at [7, 89, 19, 9]
T4 is located at [32, 68, 11, 4]
T5 is located at [46, 76, 14, 6]
T6 is located at [71, 70, 15, 9]
T7 is located at [75, 49, 22, 7]
T8 is located at [73, 30, 25, 10]
T9 is located at [58, 24, 10, 5]
T10 is located at [28, 22, 12, 5]
T11 is located at [18, 4, 66, 9]

Caption:
"""

AUDITOR_PROMPT_biology = """Given a caption and a layout of a diagram, you should determine if something is wrong in the diagram based on the caption. You should explain your answer. Think step-by-step as to why the diagram is correct or not.
The diagram will be described in terms of entities in the diagram, the relationships between the entities, and the location of each entity.
An entity can be an image or text. Entity locations will be in [x, y, width, height] format, where 0,0 is the top left corner and 100,100 is max image size.

Here are some rules the diagrams should follow:
All numbers should be positive, no negative numbers.
Entities should not be outside the bounds [0, 0, 100, 100].
The x coordinate + the width of an entity should not exceed 100.
The y coordinate + the height of an entity should not exceed 100.
Entities of the same type should not overlap.

Here are some examples:
Caption:
A diagram showing the food chain of an owl, starting from a plant (producer), to insects (herbivore/consumer), to a mouse (omnivore/consumer), and finally to an owl (carnivore/consumer).
Topic:
biology
Diagram Layout:
tree
Required Entities:
plant image (I0)
insect image (I1)
mouse image (I2)
owl image (I3)
"plant (producer)" text label (T0)
"insects (herbivore/consumer)" text label (T1)
"mouse (omnivore/consumer)" text label (T2)
"owl (carnivore/consumer)" text label (T3)
Entity Relationships:
I2 has an arrow to I3
T2 labels I2
I1 has an arrow to I2
T1 labels I1
T3 labels I3
I0 has an arrow to I1
T0 labels I0
Entity Locations:
I0 is located at [10, 10, 20, 20]
I1 is located at [40, 30, 20, 20]
I2 is located at [70, 50, 20, 20]
I3 is located at [100, 70, 20, 20]
T0 is located at [5, 5, 30, 5]
T1 is located at [35, 25, 30, 5]
T2 is located at [65, 45, 30, 5]
T3 is located at [95, 65, 30, 5]
What is wrong with this diagram?
The chain should be in a straight line.

Caption:
A diagram showing the food chain in a mountainous area, illustrating the relationships among different animals. It includes a mountain lion, a hawk, a frog, a deer, a snake, a rabbit, a cricket, a mouse, grass, and trees. The arrows in the diagram indicate the flow of energy and nutrients. It also indicates that the snake is a king cobra.
Topic:
biology
Diagram Layout:
tree
Required Entities:
mountain lion image (I0)
hawk image (I1)
frog image (I2)
deer image (I3)
snake image (I4)
rabbit image (I5)
cricket image (I6)
mouse image (I7)
grass image (I8)
tree image (I9)
"mountain lion" text label (T0)
"hawk" text label (T1)
"frog" text label (T2)
"deer" text label (T3)
"snake" text label (T4)
"rabbit" text label (T5)
"cricket" text label (T6)
"mouse" text label (T7)
"grass" text label (T8)
"trees" text label (T9)
"king cobra" text label (T10)
Entity Relationships:
T2 labels I2
T4 labels I4
I6 has an arrow to I2
T7 labels I7
T0 labels I0
T5 labels I5
I7 has an arrow to I5
T8 labels I8
T10 labels I4
I4 has an arrow to I0
I9 has an arrow to I6
I5 has an arrow to I4
I8 has an arrow to I7
I3 has an arrow to I0
T6 labels I6
T9 labels I9
I2 has an arrow to I1
T1 labels I1
T3 labels I3
Entity Locations:
I0 is located at [80, 0, 20, 20]
I1 is located at [60, 20, 20, 20]
I2 is located at [40, 40, 20, 20]
I3 is located at [20, 20, 20, 20]
I4 is located at [60, 60, 20, 20]
I5 is located at [40, 80, 20, 20]
I6 is located at [20, 60, 20, 20]
I7 is located at [0, 80, 20, 20]
I8 is located at [0, 40, 20, 20]
I9 is located at [0, 0, 20, 20]
T0 is located at [85, 5, 15, 5]
T1 is located at [65, 25, 10, 5]
T2 is located at [45, 45, 10, 5]
T3 is located at [25, 25, 10, 5]
T4 is located at [65, 65, 10, 5]
T5 is located at [45, 85, 10, 5]
T6 is located at [25, 65, 10, 5]
T7 is located at [5, 85, 10, 5]
T8 is located at [5, 45, 10, 5]
T9 is located at [5, 5, 10, 5]
T10 is located at [65, 75, 15, 5]
What is wrong with this diagram?
The snake should have an arrow the to the mountain lion and the king cobra text. The grass and tree images should have an arrow to the deer. The rabbit should have an arrow to the hawk and the mountain lion. The grass should have an arrow the cricket. The mouse should not have an arrow the rabbit, and should instead have an arrow the hawk.

Caption:
A diagram showing the food chain in a mountainous area, illustrating the relationships among different animals. It includes a mountain lion, a hawk, a frog, a deer, a snake, a rabbit, a cricket, a mouse, grass, and trees. The arrows in the diagram indicate the flow of energy and nutrients.
Topic:
biology
Diagram Layout:
tree
Required Entities:
mountain lion image (I0)
hawk image (I1)
frog image (I2)
deer image (I3)
snake image (I4)
rabbit image (I5)
cricket image (I6)
mouse image (I7)
grass image (I8)
tree image (I9)
"mountain lion" text label (T0)
"hawk" text label (T1)
"frog" text label (T2)
"deer" text label (T3)
"snake" text label (T4)
"rabbit" text label (T5)
"cricket" text label (T6)
"mouse" text label (T7)
"grass" text label (T8)
"trees" text label (T9)
Entity Relationships:
I1 has an arrow to I0
T2 labels I2
T4 labels I4
I4 has an arrow to I1
I6 has an arrow to I2
T7 labels I7
T0 labels I0
T5 labels I5
I7 has an arrow to I5
T8 labels I8
I5 has an arrow to I3
I9 has an arrow to I6
I8 has an arrow to I7
I3 has an arrow to I0
I2 has an arrow to I4
T6 labels I6
T9 labels I9
T1 labels I1
T3 labels I3
Entity Locations:
I0 is located at [80, 0, 20, 20]
I1 is located at [60, 20, 20, 20]
I2 is located at [40, 40, 20, 20]
I3 is located at [20, 60, 20, 20]
I4 is located at [60, 60, 20, 20]
I5 is located at [0, 80, 20, 20]
I6 is located at [40, 80, 20, 20]
I7 is located at [80, 80, 20, 20]
I8 is located at [20, 100, 20, 20]
I9 is located at [60, 100, 20, 20]
T0 is located at [85, 5, 15, 5]
T1 is located at [65, 25, 15, 5]
T2 is located at [45, 45, 15, 5]
T3 is located at [25, 65, 15, 5]
T4 is located at [65, 65, 15, 5]
T5 is located at [5, 85, 15, 5]
T6 is located at [45, 85, 15, 5]
T7 is located at [85, 85, 15, 5]
T8 is located at [25, 105, 15, 5]
T9 is located at [65, 105, 15, 5]
What is wrong with this diagram?
The hawk does not need an arrow to the mountain lion. The mouse and the frog need an arrow to the hawk. The trees and the grass need an arrow to the deer. The rabbit needs an arrow to the hawk and the mountain lion, not the mouse.

Caption:
A diagram showing a simplified illustration of the relationships between different biological organisms, starting with a plant, then a caterpillar, mouse, squirrel, chicken, organism Q and P, snake, organism R and S, and finally, hawk. It also includes arrows, indicating the connections between these organisms.
Topic:
biology
Diagram Layout:
tree
Required Entities:
plant image (I0)
caterpillar image (I1)
mouse image (I2)
squirrel image (I3)
chicken image (I4)
organism q image (I5)
organism p image (I6)
snake image (I7)
organism r image (I8)
organism s image (I9)
hawk image (I10)
"plant" text label (T0)
"caterpillar" text label (T1)
"mouse" text label (T2)
"squirrel" text label (T3)
"chicken" text label (T4)
"organism q" text label (T5)
"organism p" text label (T6)
"snake" text label (T7)
"organism r" text label (T8)
"organism s" text label (T9)
"hawk" text label (T10)
Entity Relationships:
T10 labels I10
T2 labels I2
I1 has an arrow to I2
T4 labels I4
I9 has an arrow to I10
I0 has an arrow to I1
I5 has an arrow to I6
T7 labels I7
I7 has an arrow to I8
T0 labels I0
T5 labels I5
I2 has an arrow to I3
T8 labels I8
T6 labels I6
I6 has an arrow to I7
T9 labels I9
I8 has an arrow to I9
I3 has an arrow to I4
T1 labels I1
T3 labels I3
I4 has an arrow to I5
Entity Locations:
I0 is located at [0, 0, 10, 10]
I1 is located at [15, 10, 10, 10]
I2 is located at [30, 20, 10, 10]
I3 is located at [45, 30, 10, 10]
I4 is located at [60, 40, 10, 10]
I5 is located at [75, 50, 10, 10]
I6 is located at [90, 60, 10, 10]
I7 is located at [75, 70, 10, 10]
I8 is located at [60, 80, 10, 10]
I9 is located at [45, 90, 10, 10]
I10 is located at [30, 100, 10, 10]
T0 is located at [0, 15, 10, 5]
T1 is located at [15, 25, 10, 5]
T2 is located at [30, 35, 10, 5]
T3 is located at [45, 45, 10, 5]
T4 is located at [60, 55, 10, 5]
T5 is located at [75, 65, 10, 5]
T6 is located at [90, 75, 10, 5]
T7 is located at [75, 85, 10, 5]
T8 is located at [60, 95, 10, 5]
T9 is located at [45, 105, 10, 5]
T10 is located at [30, 115, 10, 5]
What is wrong with this diagram?
The plant needs arrows to the mouse and squirrel. The mouse should not have an arrow the squirrel. Squirrel needs arrow to the hawk. The chicken needs an arrow to the snake. The caterpillar needs an arrow to the chicken.

Caption:
A diagram showing the life cycle of a water flea, through four different stages: egg, larva, pupa, and adult.
Topic:
biology
Diagram Layout:
circular
Required Entities:
egg image (I0)
larva image (I1)
pupa image (I2)
adult water flea image (I3)
"egg" text label (T0)
"larva" text label (T1)
"pupa" text label (T2)
"adult" text label (T3)
Entity Relationships:
T2 labels I2
T1 labels I1
T0 labels I0
T3 labels I3
Entity Locations:
I0 is located at [10, 50, 20, 20]
I1 is located at [40, 10, 20, 20]
I2 is located at [70, 50, 20, 20]
I3 is located at [40, 90, 20, 20]
T0 is located at [15, 45, 10, 5]
T1 is located at [45, 5, 10, 5]
T2 is located at [75, 45, 10, 5]
T3 is located at [45, 85, 10, 5]
What is wrong with this diagram?
There should be arrows between each phase. The adult water flea is also out of bounds, it should slightly more up so it is not outside the diagram.

Caption:
A diagram showing a consumption relationship between different types of organisms, including man, birds, duck, chicken, beetle, worm, corn, guava, pechay, and bacteria/fungi.
Topic:
biology
Diagram Layout:
tree
Required Entities:
man image (I0)
bird image (I1)
duck image (I2)
chicken image (I3)
beetle image (I4)
worm image (I5)
corn image (I6)
guava image (I7)
pechay image (I8)
bacteria/fungi image (I9)
"man" text label (T0)
"birds" text label (T1)
"duck" text label (T2)
"chicken" text label (T3)
"beetle" text label (T4)
"worm" text label (T5)
"corn" text label (T6)
"guava" text label (T7)
"pechay" text label (T8)
"bacteria/fungi" text label (T9)
Entity Relationships:
I1 has an arrow to I0
T2 labels I2
T4 labels I4
I6 has an arrow to I5
I4 has an arrow to I1
T7 labels I7
I9 has an arrow to I7
I2 has an arrow to I0
T0 labels I0
T5 labels I5
I7 has an arrow to I5
T8 labels I8
I9 has an arrow to I8
I9 has an arrow to I6
I5 has an arrow to I4
I3 has an arrow to I0
I8 has an arrow to I5
T6 labels I6
T9 labels I9
T1 labels I1
T3 labels I3
Entity Locations:
I0 is located at [50, 0, 20, 20]
I1 is located at [30, 20, 15, 15]
I2 is located at [50, 20, 15, 15]
I3 is located at [70, 20, 15, 15]
I4 is located at [20, 40, 15, 15]
I5 is located at [50, 40, 15, 15]
I6 is located at [20, 60, 15, 15]
I7 is located at [50, 60, 15, 15]
I8 is located at [80, 60, 15, 15]
I9 is located at [50, 80, 15, 15]
T0 is located at [55, 5, 10, 5]
T1 is located at [32, 35, 10, 5]
T2 is located at [52, 35, 10, 5]
T3 is located at [72, 35, 10, 5]
T4 is located at [22, 55, 10, 5]
T5 is located at [52, 55, 10, 5]
T6 is located at [22, 75, 10, 5]
T7 is located at [52, 75, 10, 5]
T8 is located at [82, 75, 10, 5]
T9 is located at [52, 95, 15, 5]
What is wrong with this diagram?
Worm needs an arrow to the chicken and birds. Corn needs an arrow to the duck, the chicken, and the birds. The guava needs an arrow to the worm and the beetle.

Caption:
A diagram showing three food chains. The first chain is flowers and grass being consumed by a rabbit and then the rabbit being consumed by a fox. The second is wheat going to field mice going to a hawk. The third one is fruit trees going to deer which goes to a bear.
Topic:
biology
Diagram Layout:
tree
Required Entities:
"flowers and grass" text label (T0)
"rabbit" text label (T1)
"fox" text label (T2)
"wheat" text label (T3)
"field mice" text label (T4)
"hawk" text label (T5)
"fruit trees" text label (T6)
"deer" text label (T7)
"bear" text label (T8)
rabbit image (I0)
fox image (I1)
field mice image (I2)
hawk image (I3)
deer image (I4)
bear image (I5)
Entity Relationships:
I2 has an arrow to I3
T5 labels I3
I4 has an arrow to I5
T8 labels I5
T7 labels I4
T4 labels I2
T2 labels I1
T1 labels I0
T3 has an arrow to I2
T0 has an arrow to I0
T6 has an arrow to I4
I0 has an arrow to I1
Entity Locations:
T0 is located at [5, 10, 20, 5]
T1 is located at [30, 20, 10, 5]
T2 is located at [50, 30, 10, 5]
T3 is located at [5, 50, 10, 5]
T4 is located at [30, 60, 15, 5]
T5 is located at [50, 70, 10, 5]
T6 is located at [5, 90, 15, 5]
T7 is located at [30, 80, 10, 5]
T8 is located at [50, 90, 10, 5]
I0 is located at [25, 15, 15, 10]
I1 is located at [45, 25, 15, 10]
I2 is located at [25, 55, 15, 10]
I3 is located at [45, 65, 15, 10]
I4 is located at [25, 85, 15, 10]
I5 is located at [45, 95, 15, 10]
What is wrong with this diagram?
Each food chain should be in a straight line. The base of each food chain should also have an image. Flowers and grass should be seperated into their own entities.

"""

DIAGRAM_PROMPT_engineering = """Given a caption of a diagram and topic, generate the diagram layout, and then a list of required entities that would be needed to create the described diagram. Then generate a list of the relationships between the entities (i.e. which ones are connected or labeling each other). Finally, generate the location of each entity.
An entity can be an image or text. Entity locations should be generated in [x, y, width, height] format, where 0,0 is the top left corner and 100,100 is max image size.

Think step-by-step, break each caption into parts and generate the required entities, relationships, and locations for each part.

Here are some rules to follow:
All numbers should be positive, do not generate negative numbers.
Please always generate a list of entities, even if the list is empty.
Entities should not be outside the bounds [0, 0, 100, 100].
The x coordinate + the width of an entity should not exceed 100.
The y coordinate + the height of an entity should not exceed 100.
Entities of the same type should not overlap.

Here are some examples:

Caption:
A diagram showing two simple circuits with a battery and three lights. One circuit has a switch to control the flow of electricity. Both circuits are connects in series.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
battery image (I0)
"battery" text label (T0)
"switch" text label (T1)
switch image (I1)
light bulb image (I2)
light bulb image (I3)
light bulb image (I4)
battery image (I5)
light bulb image (I6)
light bulb image (I7)
light bulb image (I8)
Entity Relationships:
I6 connects to I7
T1 labels I1
I0 connects to I1
I3 connects to I4
I5 connects to I6
I7 connects to I8
I8 connects to I5
I4 connects to I0
I2 connects to I3
T0 labels I0
I1 connects to I2
Entity Locations:
I0 is located at [0, 62, 7, 20]
T0 is located at [10, 69, 11, 7]
T1 is located at [10, 9, 10, 6]
I1 is located at [9, 17, 16, 14]
I2 is located at [27, 3, 14, 27]
I3 is located at [27, 35, 15, 26]
I4 is located at [26, 65, 15, 27]
I5 is located at [58, 33, 9, 28]
I6 is located at [73, 7, 7, 20]
I7 is located at [88, 43, 10, 12]
I8 is located at [74, 56, 7, 20]

Caption:
A diagram showing two circuits. In both a circuits, there are two light bulbs connected to a battery. The first circuit is in series and the second one is in parallel.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
battery image (I0)
light bulb image (I1)
light bulb image (I2)
light bulb image (I3)
light bulb image (I4)
battery image (I5)
Entity Relationships:
I4 connects to I5
I0 connects to I1
I4 connects to I3
I3 connects to I4
I5 connects to I4
I1 connects to I2
Entity Locations:
I0 is located at [17, 18, 22, 13]
I1 is located at [13, 46, 13, 27]
I2 is located at [28, 47, 14, 24]
I3 is located at [66, 71, 16, 25]
I4 is located at [68, 30, 14, 26]
I5 is located at [64, 3, 21, 12]

Caption:
A diagram showing a simple electric circuit with a battery, a light bulb, and a switch.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
light bulb image (I0)
battery image (I1)
switch image (I2)
"simple electric circuit" text label (T0)
Entity Relationships:
I1 connects to I2
I0 connects to I1
I2 connects to I0
Entity Locations:
I0 is located at [18, 22, 17, 26]
I1 is located at [30, 74, 40, 12]
I2 is located at [66, 38, 10, 9]
T0 is located at [5, 5, 90, 7]

Caption:
A diagram showing a simple circuit with a battery and three light bulbs. The lights and battery are connected in series.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
battery image (I0)
light bulb image (I1)
light bulb image (I2)
light bulb image (I3)
Entity Relationships:
I1 connects to I2
I2 connects to I3
I0 connects to I1
I3 connects to I0
Entity Locations:
I0 is located at [10, 37, 12, 37]
I1 is located at [44, 61, 14, 29]
I2 is located at [77, 37, 14, 29]
I3 is located at [43, 3, 14, 28]

Caption:
A diagram showing a circuit schematic. The 10V better is connected to a 1 ohm resistor directly. Then the 1 ohm resistor is connected to a 25 ohm resistor and 30 ohm resistor in parallel. Those resistors are connected to a 50 ohm and 55 ohm resistor respectively. Then the parallel circuit comes back together and connects to the battery. Both sides of the parallel circuit are connected via a 1 ohm resistor.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
"10v" text label (T0)
"1 ohm" text label (T1)
"25 ohm" text label (T2)
"50 ohm" text label (T3)
"1 ohm" text label (T4)
"30 ohm" text label (T5)
"55 ohm" text label (T6)
battery schematic image (I0)
resistor schematic image (I1)
resistor schematic image (I2)
resistor schematic image (I3)
resistor schematic image (I4)
resistor schematic image (I5)
resistor schematic image (I6)
Entity Relationships:
T0 labels I0
T2 labels I2
T6 labels I6
T5 labels I5
T1 labels I1
T4 labels I4
T3 labels I3
Entity Locations:
T0 is located at [1, 40, 9, 8]
T1 is located at [26, 11, 8, 9]
T2 is located at [53, 26, 9, 8]
T3 is located at [38, 72, 10, 7]
T4 is located at [62, 58, 8, 7]
T5 is located at [90, 27, 9, 8]
T6 is located at [89, 71, 9, 8]
I0 is located at [8, 48, 9, 7]
I1 is located at [25, 2, 12, 9]
I2 is located at [48, 21, 5, 17]
I3 is located at [48, 66, 6, 18]
I4 is located at [62, 46, 12, 9]
I5 is located at [83, 21, 6, 19]
I6 is located at [83, 64, 6, 20]

Caption:
A diagram showing a circuit with a 6V battery being connected to 2 light bulbs on opposite sides and then a switch in between them. The switch then connects to both light bulbs.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
battery image (I0)
switch image (I1)
light bulb on image (I2)
light bulb off image (I3)
"6v" text label (T0)
Entity Relationships:
T0 labels I0
I2 connects to I1
I0 connects to I1
I3 connects to I1
I0 connects to I2
I0 connects to I3
Entity Locations:
I0 is located at [9, 40, 11, 21]
I1 is located at [30, 37, 66, 26]
I2 is located at [66, 0, 10, 20]
I3 is located at [66, 75, 10, 21]
T0 is located at [12, 35, 6, 5]

Caption:
A diagram showing the components of a slipper spring. It includes a spring hanger, a spring bolt and locknut, a two rebound clips, a slipper, and a centre bolt.
Topic:
engineering
Diagram Layout:
abstract
Required Entities:
spring hanger image (I0)
spring bolt and locknut image (I1)
rebound clip image (I2)
rebound clip image (I3)
slipper image (I4)
"spring hanger" text label (T0)
"spring bolt & locknut" text label (T1)
"rebound clip" text label (T2)
"slipper" text label (T3)
"centre bolt" text label (T4)
centre bolt image (I5)
"eye/slipper spring components" text label (T5)
Entity Relationships:
T0 labels I0
T3 labels I4
T2 labels I2
T4 labels I5
T2 labels I3
T1 labels I1
Entity Locations:
I0 is located at [6, 18, 8, 24]
I1 is located at [7, 29, 4, 11]
I2 is located at [22, 56, 5, 18]
I3 is located at [65, 49, 6, 16]
I4 is located at [81, 17, 16, 16]
T0 is located at [16, 6, 15, 8]
T1 is located at [2, 72, 20, 7]
T2 is located at [75, 77, 13, 8]
T3 is located at [67, 2, 7, 6]
T4 is located at [42, 91, 11, 6]
I5 is located at [45, 64, 3, 15]
T5 is located at [61, 91, 33, 8]

Caption:
A diagram showing a simple electronic circuit with a lamp and a battery.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
lamp image (I0)
battery image (I1)
"lamp" text label (T0)
"battery" text label (T1)
Entity Relationships:
T1 labels I1
I0 connects to I1
I1 connects to I0
T0 labels I0
Entity Locations:
I0 is located at [32, 12, 28, 38]
I1 is located at [27, 65, 31, 22]
T0 is located at [31, 2, 14, 7]
T1 is located at [28, 90, 21, 7]

Caption:
A diagram showing the flow of energy through various processes, including energy conversion, storage, and distribution. Each process is represented as a block. It also shows the sun as an energy source going into the energy conversion, and energy use as a light bulb and electric utility as powerlines coming out of the energy distribution.
Topic:
engineering
Diagram Layout:
tree
Required Entities:
sun image (I0)
metal plate image (I1)
block image (I2)
block image (I3)
light bulb image (I4)
block image (I5)
powerline image (I6)
"energy source" text label (T0)
"energy conversion" text label (T1)
"energy storage" text label (T2)
"energy inversion & conditioning" text label (T3)
"energy use" text label (T4)
"energy distribution" text label (T5)
"electric utility" text label (T6)
Entity Relationships:
I3 has an arrow to I2
T0 labels I0
I6 has an arrow to I5
I2 has an arrow to I3
T2 labels I2
I2 has an arrow to I5
I5 has an arrow to I6
T6 labels I6
I0 has an arrow to I1
I1 has an arrow to I2
T5 labels I5
I5 has an arrow to I4
T1 labels I1
T4 labels I4
T3 labels I3
Entity Locations:
I0 is located at [0, 2, 11, 20]
I1 is located at [9, 38, 20, 17]
I2 is located at [44, 28, 12, 35]
I3 is located at [43, 78, 16, 20]
I4 is located at [70, 2, 12, 20]
I5 is located at [72, 37, 10, 18]
I6 is located at [69, 71, 18, 28]
T0 is located at [1, 26, 10, 11]
T1 is located at [10, 57, 15, 11]
T2 is located at [30, 83, 12, 14]
T3 is located at [43, 11, 16, 18]
T4 is located at [83, 8, 11, 12]
T5 is located at [82, 39, 17, 14]
T6 is located at [87, 78, 10, 15]

Caption:
A diagram showing a battery with a light bulb connected to it.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
light bulb image (I0)
battery image (I1)
Entity Relationships:
I0 connects to I1
I1 connects to I0
Entity Locations:
I0 is located at [8, 4, 22, 41]
I1 is located at [66, 40, 27, 39]

Caption:
"""

AUDITOR_PROMPT_engineering = """Given a caption and a layout of a diagram, you should determine if something is wrong in the diagram based on the caption. You should explain your answer. Think step-by-step as to why the diagram is correct or not.
The diagram will be described in terms of entities in the diagram, the relationships between the entities, and the location of each entity.
An entity can be an image or text. Entity locations will be in [x, y, width, height] format, where 0,0 is the top left corner and 100,100 is max image size.

Here are some rules the diagrams should follow:
All numbers should be positive, no negative numbers.
Entities should not be outside the bounds [0, 0, 100, 100].
The x coordinate + the width of an entity should not exceed 100.
The y coordinate + the height of an entity should not exceed 100.
Entities of the same type should not overlap.

Here are some examples:
Caption:
A diagram showing a simple electrical circuit schematic with a battery, a switch, and two light bulbs.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
battery schematic image (I0)
light bulb schematic image (I1)
light bulb schematic image (I2)
"simple electrical circuit" text label (T0)
Entity Relationships:
I2 connects to I0
I1 connects to I2
I0 connects to I1
T0 labels I0
Entity Locations:
I0 is located at [10, 40, 20, 20]
I1 is located at [40, 10, 20, 20]
I2 is located at [70, 40, 20, 20]
T0 is located at [10, 70, 80, 10]
What is wrong with this diagram?
The switch is missing from the circuit in this diagram.

Caption:
A diagram showing the cross-section of a cable with different components, including rubber insulator and copper conductor.
Topic:
engineering
Diagram Layout:
abstract
Required Entities:
cross-section of cable image (I0)
rubber insulator image (I1)
copper conductor image (I2)
"rubber insulator" text label (T0)
"copper conductor" text label (T1)
Entity Relationships:
T1 labels I2
T0 labels I1
Entity Locations:
I0 is located at [0, 0, 100, 100]
I1 is located at [20, 40, 20, 20]
I2 is located at [60, 40, 20, 20]
T0 is located at [20, 65, 20, 10]
T1 is located at [60, 65, 25, 10]
What is wrong with this diagram?
The copper conductor should be inside of the rubber insulator. The rubber insulator should be a bit bigger.

Caption:
A diagram showing a simple electronic circuit schematic with a battery and a resistor.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
battery schematic image (I0)
resistor schematic image (I1)
"battery" text label (T0)
"resistor" text label (T1)
Entity Relationships:
T1 labels I1
I0 connects to I1
T0 labels I0
Entity Locations:
I0 is located at [10, 40, 20, 20]
I1 is located at [60, 40, 20, 20]
T0 is located at [10, 65, 20, 10]
T1 is located at [60, 65, 20, 10]
What is wrong with this diagram?
There should a connection from I1 to I0 as well.

Caption:
A diagram showing a circuit with two light bulbs and a battery connect in parallel. There is also a schematic diagram of the circuit.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
light bulb image (I0)
light bulb image (I1)
battery image (I2)
circuit schematic image (I3)
Entity Relationships:
I2 connects to I0
I0 connects to I2
I1 connects to I2
I2 connects to I1
Entity Locations:
I0 is located at [10, 20, 20, 30]
I1 is located at [10, 60, 20, 30]
I2 is located at [40, 40, 20, 20]
I3 is located at [70, 40, 20, 20]
What is wrong with this diagram?
The light bulbs should also be connected to each other. The image of a circuit schematic should actually have 3 entities that have the same connections as the actual circuit.

Caption:
A diagram showing a simple circuit schematic with a battery, light bulb, and a switch all connected in series.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
battery image (I0)
light bulb image (I1)
switch image (I2)
"simple circuit schematic" text label (T0)
Entity Relationships:
I2 connects to I0
I1 connects to I2
I0 connects to I1
Entity Locations:
I0 is located at [10, 40, 20, 20]
I1 is located at [40, 40, 20, 20]
I2 is located at [70, 40, 20, 20]
T0 is located at [10, 10, 80, 10]
What is wrong with this diagram?
The components of the circuit should form a loop rather than straight line.

Caption:
A diagram showing a simple circuit with two light bulbs and a battery. The light bulbs are connected parallel with the battery.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
light bulb image (I0)
light bulb image (I1)
battery image (I2)
Entity Relationships:
I0 connects to I2
I1 connects to I2
Entity Locations:
I0 is located at [10, 30, 20, 30]
I1 is located at [70, 30, 20, 30]
I2 is located at [40, 50, 20, 30]
What is wrong with this diagram?
The battery should connect to both light bulbs and the light bulbs should connect to each other.

Caption:
A diagram showing two circuits. The first is a open circuit with a light bulb connected to battery but the battery doesn't have a connection to the light bulb. The second is a closed circuit with a light bulb connected to a battery and the battery returns the connection.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
light bulb image (I0)
battery image (I1)
light bulb image (I2)
battery image (I3)
"open circuit" text label (T0)
"closed circuit" text label (T1)
Entity Relationships:
I2 connects to I3
I1 connects to I0
I3 connects to I2
Entity Locations:
I0 is located at [10, 20, 15, 25]
I1 is located at [10, 60, 15, 25]
I2 is located at [60, 20, 15, 25]
I3 is located at [60, 60, 15, 25]
T0 is located at [30, 30, 20, 10]
T1 is located at [80, 70, 20, 10]
What is wrong with this diagram?
The open and closed circuit text labels should be above each circuit, not besides them.

Caption:
A diagram showing a electrical circuit schematic. It has a 12V battery connected to a 1k resistor, a light bulb, and another 1k resistor.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
"12v" text label (T0)
"1k" text label (T1)
"1k" text label (T2)
battery schematic image (I0)
resistor schematic image (I1)
light bulb schematic image (I2)
resistor schematic image (I3)
Entity Relationships:
I3 connects to I0
I1 connects to I2
I2 connects to I3
T1 labels I1
I0 connects to I1
T0 labels I0
T2 labels I3
Entity Locations:
T0 is located at [2, 40, 8, 7]
T1 is located at [20, 10, 8, 7]
T2 is located at [80, 10, 8, 7]
I0 is located at [10, 50, 15, 10]
I1 is located at [30, 20, 10, 10]
I2 is located at [50, 50, 10, 10]
I3 is located at [70, 20, 10, 10]
What is wrong with this diagram?
The light bulb schematic and the resistor schematic should swap places to make the diagram flow smoother.

Caption:
A diagram showing the structure of an electric circuit with a light bulb, a switch, and a battery.
Topic:
engineering
Diagram Layout:
circular
Required Entities:
light bulb image (I0)
battery image (I1)
"electric circuit" text label (T0)
Entity Relationships:
T0 labels I0 and I1
I0 connects to I1
I1 connects to I0
Entity Locations:
I0 is located at [10, 30, 20, 40]
I1 is located at [70, 30, 20, 40]
T0 is located at [40, 50, 20, 10]
What is wrong with this diagram?
The switch is missing from the circuit in this diagram.

"""

prompts = {'diagram_astronomy': DIAGRAM_PROMPT_astronomy,'auditor_astronomy': AUDITOR_PROMPT_astronomy,'diagram_biology': DIAGRAM_PROMPT_biology,'auditor_biology': AUDITOR_PROMPT_biology, 'diagram_engineering': DIAGRAM_PROMPT_engineering,'auditor_engineering': AUDITOR_PROMPT_engineering,}