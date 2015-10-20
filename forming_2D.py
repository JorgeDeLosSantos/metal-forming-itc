# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import time

# Define constants
MODEL_NAME = "2D-MODEL"
STEP_PATH = "C:/Users/User/Desktop/LABPro/PI1501 - Rassini-Bypasa/geom/stp/"
STEP_FILES = ["sketch_lower_02","sketch_lower_03","sketch_lower_left_01","sketch_lower_right_01",
			"sketch_pisador","sketch_upper_03","sketch_upper_left_01","sketch_upper_right_01",
			"sketch_upper_left_02","sketch_upper_right_02"]
DYNEXP_STEPS = ["Initial","Step-01-Down","Step-01-Up","Step-02-Down","Step-02-Up","Step-03-Down","Step-03-Up"]
NFRAMES = 50.0
TIME_PERIOD = 0.86
YDISP = 1.428
MESH_SIZE_QUAD = 0.02
MESH_SIZE_TRI = 0.025
JOB_NAME = "MSZ-"+str(MESH_SIZE_QUAD).replace(".","")+time.strftime("_%d-%m-%Y-%H%M",time.localtime())

mdb.models.changeKey(fromName='Model-1', toName=MODEL_NAME)

# Define parts 
# Blank
mdb.openStep(STEP_PATH + 'sketch_mp.STEP', scaleFromFile=OFF)
mdb.models[MODEL_NAME].ConstrainedSketchFromGeometryFile(geometryFile=mdb.acis, name='plate')
mdb.models[MODEL_NAME].ConstrainedSketch(name='__profile__', sheetSize=10.0)
mdb.models[MODEL_NAME].sketches['__profile__'].sketchOptions.setValues(gridOrigin=(0.0, 0.0))
mdb.models[MODEL_NAME].sketches['__profile__'].retrieveSketch(sketch=mdb.models[MODEL_NAME].sketches['plate'])
mdb.models[MODEL_NAME].Part(dimensionality=TWO_D_PLANAR, name='plate', type=DEFORMABLE_BODY)
mdb.models[MODEL_NAME].parts['plate'].BaseShell(sketch=mdb.models[MODEL_NAME].sketches['__profile__'])
del mdb.models[MODEL_NAME].sketches['__profile__']

# Analytic surfaces
for _stp in STEP_FILES:
	mdb.openStep(STEP_PATH + _stp + ".STEP", scaleFromFile=OFF)
	mdb.models[MODEL_NAME].ConstrainedSketchFromGeometryFile(geometryFile=mdb.acis, name=_stp)
	mdb.models[MODEL_NAME].ConstrainedSketch(name='__profile__', sheetSize=10.0)
	mdb.models[MODEL_NAME].sketches['__profile__'].sketchOptions.setValues(gridOrigin=(0.0, 0.0))
	mdb.models[MODEL_NAME].sketches['__profile__'].retrieveSketch(sketch=mdb.models[MODEL_NAME].sketches[_stp])
	mdb.models[MODEL_NAME].Part(dimensionality=TWO_D_PLANAR, name=_stp[7::], type=ANALYTIC_RIGID_SURFACE)
	mdb.models[MODEL_NAME].parts[_stp[7::]].AnalyticRigidSurf2DPlanar(sketch=mdb.models[MODEL_NAME].sketches['__profile__'])
	del mdb.models[MODEL_NAME].sketches['__profile__']

# Material 	
mdb.models[MODEL_NAME].Material(name='Acero 1018 US')
mdb.models[MODEL_NAME].materials['Acero 1018 US'].Density(table=((0.10555, ), 
    ))
mdb.models[MODEL_NAME].materials['Acero 1018 US'].Elastic(table=((29700000.0, 
    0.33), ))
mdb.models[MODEL_NAME].materials['Acero 1018 US'].Plastic(table=((50800.03458, 
    0.0), (51320.13977, 0.82), (51376.4144, 0.841), (51781.35965, 0.898), (
    51784.84056, 0.92), (52105.22884, 0.977), (52140.03789, 0.999), (
    52442.8766, 1.056), (52529.17404, 1.078), (52876.8294, 1.135), (
    52988.79851, 1.157), (53391.85827, 1.213), (53507.88843, 1.236), (
    53929.8031, 1.292), (54093.40563, 1.315), (54475.57997, 1.371), (
    54659.92289, 1.394), (55019.18127, 1.45), (55191.92117, 1.473), (
    55558.2864, 1.528), (55721.59885, 1.551), (56028.93374, 1.607), (
    56243.58953, 1.63), (56553.82517, 1.686), (56798.35873, 1.709), (
    57048.25869, 1.764), (57256.53283, 1.788), (57509.91369, 1.843), (
    57744.43965, 1.867), (57970.26335, 1.922), (58210.01067, 1.946), (
    58405.23141, 2.0), (58661.22295, 2.025), (58860.35972, 2.079), (
    59113.88562, 2.104), (59211.64103, 2.158), (59521.15148, 2.183), (
    59624.27328, 2.236), (59925.51658, 2.262), (59986.72249, 2.315), (
    60343.08012, 2.341), (60397.46926, 2.394), (60699.58279, 2.42), (
    60755.27727, 2.472), (61121.35242, 2.498), (61126.2837, 2.551), (
    61471.90854, 2.577), (61499.75578, 2.63), (61825.65549, 2.656), (
    62178.96733, 2.735), (62518.50059, 2.814), (62831.05683, 2.893), (
    63136.65126, 2.971), (63479.37535, 3.05), (63745.51953, 3.129), (
    64049.08343, 3.208), (64353.37253, 3.287), (64638.22657, 3.365), (
    64915.68369, 3.444), (65132.07994, 3.523), (65419.25459, 3.601), (
    65630.42948, 3.68), (65650.44468, 3.702), (65905.85607, 3.759), (
    66157.78655, 3.838), (66380.12935, 3.917), (66405.22087, 3.939), (
    66614.07516, 3.995), (66626.69344, 4.018), (66811.47147, 4.074), (
    66847.73089, 4.096), (67017.27996, 4.153), (67059.05082, 4.175), (
    67223.81365, 4.232), (67244.98915, 4.254), (67412.21762, 4.31), (
    67430.63741, 4.333), (67593.65978, 4.389), (67648.48403, 4.412), (
    67801.64385, 4.468), (67842.39944, 4.491), (67989.75774, 4.547), (
    68045.45222, 4.57), (68147.55876, 4.625), (68235.74168, 4.649), (
    68309.85595, 4.704), (68399.77932, 4.727), (68457.64936, 4.782), (
    68573.67952, 4.807), (68624.44272, 4.861), (68734.96144, 4.885), (
    68763.67891, 4.94), (68878.40373, 4.964), (68931.05242, 5.019), (
    69078.26568, 5.043), (69230.7003, 5.122), (69405.18066, 5.201), (69521.936, 
    5.28), (69665.95844, 5.359), (69781.40845, 5.438), (69915.13321, 5.517), (
    70051.75872, 5.595), (70168.51407, 5.674), (70323.41434, 5.753), (
    70415.65831, 5.832), (70540.39073, 5.911), (70648.00871, 5.989), (
    70769.5503, 6.068), (70848.0157, 6.147), (70950.55735, 6.226), (
    71035.11433, 6.305), (71122.42702, 6.384), (71228.44958, 6.462), (
    71316.92258, 6.541), (71433.82297, 6.62), (71501.12046, 6.699), (
    71590.31864, 6.777), (71635.57041, 6.856), (71722.01288, 6.935), (
    71798.30271, 7.014), (71877.9284, 7.092), (71923.47024, 7.171), (
    71956.24876, 7.194), (72010.05775, 7.25), (72020.06535, 7.273), (
    72045.44695, 7.329), (72086.20254, 7.352), (72130.00393, 7.407), (
    72159.01147, 7.43), (72224.27843, 7.51), (72256.76688, 7.565), (
    72294.91179, 7.588), (72343.7895, 7.667), (72402.52976, 7.746), (
    72468.23184, 7.825), (72507.53706, 7.904), (72582.08644, 7.983), (
    72584.40704, 8.062), (72681.43726, 8.141), (72731.62031, 8.22), (
    72770.78048, 8.298), (72782.23846, 8.377), (72814.72691, 8.456), (
    72891.01674, 8.535), (72944.82572, 8.614), (72957.87912, 8.693), (
    72995.00877, 8.771), (72997.90952, 8.85), (73058.82536, 8.929), (
    73082.61154, 9.008), (73141.93196, 9.087), (73161.22197, 9.244), (
    73232.14541, 9.402), (73240.70263, 9.56), (73281.7483, 9.717), (
    73347.01527, 9.796), (73350.06106, 10.347), (73396.03801, 10.425), (
    73399.0838, 10.922), (73400.82425, 11.001), (73403.87005, 11.08), (
    73414.89291, 11.159), (73416.7784, 11.237), (73221.84773, 11.261), (
    73215.46607, 11.419), (73212.27524, 11.498), (73195.45087, 11.655), (
    73166.29829, 12.0), (73143.09226, 12.078), (73120.61142, 12.157), (
    73089.13824, 12.236), (73066.07724, 12.314), (73033.87887, 12.472), (
    73014.87893, 12.55), (72980.505, 12.629), (72971.80274, 12.707), (
    72927.71128, 12.786), (72924.08533, 12.865), (72857.07792, 12.943), (
    72843.58941, 13.022), (72820.0933, 13.101), (72793.11629, 13.179), (
    72746.41415, 13.258), (72680.27696, 13.415), (72649.23889, 13.494), (
    72601.23141, 13.572), (72574.97959, 13.651), (72519.57519, 13.729), (
    72507.82713, 13.808), (72442.99528, 13.887), (72421.09459, 13.965), (
    72361.33906, 14.044), (72300.7133, 14.123), (72243.56845, 14.201), (
    72163.07252, 14.28), (72124.49249, 14.359), (72032.82867, 14.437), (
    71990.04255, 14.516), (71925.06566, 14.595), (71852.98192, 14.673), (
    71748.98989, 14.752), (71652.1047, 14.831), (71559.86073, 14.91), (
    71452.53283, 14.988), (71351.15148, 15.067), (71227.86943, 15.146), (
    71078.4806, 15.225), (70955.92374, 15.303), (70791.74107, 15.382), (
    70787.09986, 15.412), (70650.76442, 15.461), (70596.66536, 15.491), (
    70462.9406, 15.539), (70416.81861, 15.569), (70313.55177, 15.618), (
    70218.69712, 15.648), (70150.38436, 15.697), (70014.77411, 15.726), (
    69924.99577, 15.775), (69814.47705, 15.805), (69767.33979, 15.854), (
    69637.09594, 15.884), (69515.98946, 15.933), (69392.56238, 15.962), (
    69319.31834, 16.012), (69142.51738, 16.041), (69060.71612, 16.09), (
    68928.44174, 16.12), (68816.76271, 16.169), (68637.35107, 16.198), (
    68582.09171, 16.248), (68373.23742, 16.277), (68544.38191, 16.305), (
    68325.81009, 16.327), (68118.98633, 16.355), (68253.29124, 16.384), (
    68029.208, 16.405), (67845.73531, 16.434), (67980.62037, 16.462), (
    67759.87299, 16.484), (67622.9574, 16.512), (67687.78925, 16.541), (
    67462.83578, 16.563), (67273.41654, 16.591), (67412.94281, 16.62), (
    67190.74505, 16.642), (66966.66181, 16.67), (67085.73776, 16.699), (
    66852.08202, 16.721), (66597.83094, 16.748), (66758.67774, 16.778), (
    66521.68614, 16.8), (66258.29768, 16.827), (66394.77816, 16.856), (
    66174.75596, 16.878), (65891.06222, 16.906), (66038.85564, 16.935), (
    65830.00135, 16.957), (65559.07093, 16.984), (65665.09349, 17.014), (
    65456.67431, 17.036), (65210.98045, 17.063), (65342.09453, 17.092), (
    65132.37001, 17.115), (64827.50077, 17.142), (64947.73702, 17.171), (
    64732.06596, 17.194), (64440.83026, 17.22), (64575.13517, 17.25), (
    64348.15117, 17.273), (64072.86962, 17.299), (64155.39607, 17.329), (
    63938.99982, 17.351), (63648.92442, 17.377), (63737.68749, 17.407), (
    63509.9783, 17.43), (63205.39913, 17.456), (63274.29204, 17.486), (
    63073.84994, 17.509), (62738.08766, 17.535), (62830.62172, 17.565), (
    62611.46975, 17.588), (62280.05861, 17.614), (62352.86753, 17.644), (
    62131.39496, 17.667), (61823.04481, 17.692), (61841.02949, 17.722), (
    61656.68657, 17.746), (61339.92423, 17.771), (61393.44315, 17.801), (
    61191.98578, 17.825), (60844.62049, 17.85), (60879.2845, 17.88), (
    60643.30816, 17.904), (60336.55343, 17.928), (60316.68326, 17.959), (
    60104.34807, 17.983), (59781.49415, 18.007), (59765.68504, 18.037), (
    59561.32692, 18.062), (59187.12965, 18.086), (59195.68688, 18.116), (
    58989.00816, 18.14), (58618.58187, 18.164), (58581.59726, 18.194), (
    58414.36879, 18.219), (58036.2555, 18.243), (57970.40839, 18.273), (
    57758.50831, 18.298), (57411.72317, 18.322), (57320.92957, 18.352), (
    57138.3271, 18.377), (56738.89328, 18.4), (56703.35904, 18.43), (
    56482.46662, 18.456), (56095.361, 18.479), (56006.45289, 18.509), (
    55773.66738, 18.535), (55431.37841, 18.558), (55320.42457, 18.588), (
    55075.60093, 18.614), (54688.49531, 18.637), (54564.198, 18.667), (
    54344.61093, 18.692), (53943.14657, 18.715), (53824.50573, 18.745), (
    53540.0868, 18.771), (53109.1798, 18.794), (52984.01226, 18.824), (
    52730.34133, 18.85), (52306.97628, 18.873), (52121.76314, 18.903), (
    51858.66475, 18.929), (51442.26151, 18.952), (51204.39968, 18.982), (
    50952.03409, 19.008), (50487.47833, 19.03), (50252.08215, 19.06), (
    49540.52719, 19.088)))

# Steps 
for jj in range(1,len(DYNEXP_STEPS)):
	mdb.models[MODEL_NAME].ExplicitDynamicsStep(name=DYNEXP_STEPS[jj], previous=DYNEXP_STEPS[jj-1], timePeriod=0.86)
	
# Reference points
mdb.models[MODEL_NAME].parts['lower_02'].ReferencePoint(point=
    mdb.models[MODEL_NAME].parts['lower_02'].vertices[0])
mdb.models[MODEL_NAME].parts['lower_03'].ReferencePoint(point=
    mdb.models[MODEL_NAME].parts['lower_03'].vertices[0])
mdb.models[MODEL_NAME].parts['lower_left_01'].ReferencePoint(point=
    mdb.models[MODEL_NAME].parts['lower_left_01'].vertices[5])
mdb.models[MODEL_NAME].parts['lower_right_01'].ReferencePoint(point=
    mdb.models[MODEL_NAME].parts['lower_right_01'].vertices[0])
mdb.models[MODEL_NAME].parts['pisador'].ReferencePoint(point=
    mdb.models[MODEL_NAME].parts['pisador'].InterestingPoint(
    mdb.models[MODEL_NAME].parts['pisador'].edges[0], MIDDLE))
mdb.models[MODEL_NAME].parts['upper_03'].ReferencePoint(point=
    mdb.models[MODEL_NAME].parts['upper_03'].vertices[5])
mdb.models[MODEL_NAME].parts['upper_left_01'].ReferencePoint(point=
    mdb.models[MODEL_NAME].parts['upper_left_01'].vertices[0])
mdb.models[MODEL_NAME].parts['upper_left_02'].ReferencePoint(point=
    mdb.models[MODEL_NAME].parts['upper_left_02'].vertices[0])
mdb.models[MODEL_NAME].parts['upper_right_01'].ReferencePoint(point=
    mdb.models[MODEL_NAME].parts['upper_right_01'].vertices[3])
mdb.models[MODEL_NAME].parts['upper_right_02'].ReferencePoint(point=
    mdb.models[MODEL_NAME].parts['upper_right_02'].vertices[6])
	
# Partition of plate ============================================================
# Datum points
mdb.models[MODEL_NAME].parts['plate'].DatumPointByOffset(point=
    mdb.models[MODEL_NAME].parts['plate'].vertices[0], vector=(0.0, 0.06, 0.0))
mdb.models[MODEL_NAME].parts['plate'].DatumPointByOffset(point=
    mdb.models[MODEL_NAME].parts['plate'].vertices[5], vector=(0.0, 0.06, 0.0))

mdb.models[MODEL_NAME].parts['plate'].PartitionFaceByShortestPath(faces=
    mdb.models[MODEL_NAME].parts['plate'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), point1=mdb.models[MODEL_NAME].parts['plate'].vertices[4], point2=
    mdb.models[MODEL_NAME].parts['plate'].vertices[1])
mdb.models[MODEL_NAME].parts['plate'].PartitionFaceByShortestPath(faces=
    mdb.models[MODEL_NAME].parts['plate'].faces.getSequenceFromMask(('[#2 ]', 
    ), ), point1=mdb.models[MODEL_NAME].parts['plate'].vertices[4], point2=
    mdb.models[MODEL_NAME].parts['plate'].datums[3])
mdb.models[MODEL_NAME].parts['plate'].PartitionFaceByShortestPath(faces=
    mdb.models[MODEL_NAME].parts['plate'].faces.getSequenceFromMask(('[#4 ]', 
    ), ), point1=mdb.models[MODEL_NAME].parts['plate'].vertices[6], point2=
    mdb.models[MODEL_NAME].parts['plate'].datums[2])
	
mdb.models[MODEL_NAME].parts['plate'].PartitionFaceByCurvedPathEdgePoints(
    edge1=mdb.models[MODEL_NAME].parts['plate'].edges[3], edge2=
    mdb.models[MODEL_NAME].parts['plate'].edges[1], face=
    mdb.models[MODEL_NAME].parts['plate'].faces[0], point1=
    mdb.models[MODEL_NAME].parts['plate'].InterestingPoint(
    mdb.models[MODEL_NAME].parts['plate'].edges[3], MIDDLE), point2=
    mdb.models[MODEL_NAME].parts['plate'].InterestingPoint(
    mdb.models[MODEL_NAME].parts['plate'].edges[1], MIDDLE))
	
# Assembly  =========================================================================
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name='lower_02-1', 
    part=mdb.models[MODEL_NAME].parts['lower_02'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name='lower_03-1', 
    part=mdb.models[MODEL_NAME].parts['lower_03'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name=
    'lower_left_01-1', part=mdb.models[MODEL_NAME].parts['lower_left_01'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name=
    'lower_right_01-1', part=mdb.models[MODEL_NAME].parts['lower_right_01'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name='pisador-1', 
    part=mdb.models[MODEL_NAME].parts['pisador'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name='plate-1', 
    part=mdb.models[MODEL_NAME].parts['plate'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name='upper_03-1', 
    part=mdb.models[MODEL_NAME].parts['upper_03'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name=
    'upper_left_01-1', part=mdb.models[MODEL_NAME].parts['upper_left_01'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name=
    'upper_left_02-1', part=mdb.models[MODEL_NAME].parts['upper_left_02'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name=
    'upper_right_01-1', part=mdb.models[MODEL_NAME].parts['upper_right_01'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name=
    'upper_right_02-1', part=mdb.models[MODEL_NAME].parts['upper_right_02'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name=
    'lower_left_01-2', part=mdb.models[MODEL_NAME].parts['lower_left_01'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name=
    'lower_right_01-2', part=mdb.models[MODEL_NAME].parts['lower_right_01'])
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=ON, name='lower_02-2', 
    part=mdb.models[MODEL_NAME].parts['lower_02'])
	
# Translate parts
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('pisador-1', ), 
    vector=(-0.373, 0.13, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('plate-1', ), 
    vector=(0.0, 0.2845, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('lower_left_01-1', 
    ), vector=(-2.5275, 2.032495, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('lower_right_01-1', 
    ), vector=(-2.0315, 2.032495, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('upper_left_01-1', 
    ), vector=(-8.148372, 2.25428, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('upper_right_01-1', 
    ), vector=(-7.402372, 2.25428, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('upper_left_02-1', 
    'upper_right_02-1'), vector=(2.0, 1.421506, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('upper_03-1', ), 
    vector=(-10.7795, 0.637, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('lower_02-1', ), 
    vector=(-7.735, -2.5, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('lower_03-1', ), 
    vector=(-14.3255, -0.784, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('lower_left_01-2', 
    ), vector=(-2.5275, 1.532495, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('lower_right_01-2', 
    ), vector=(-2.0315, 1.532495, 0.0))
mdb.models[MODEL_NAME].rootAssembly.translate(instanceList=('lower_02-2', ), 
    vector=(-7.735, -3.0, 0.0))
	

# Surfaces ========================================================================
mdb.models[MODEL_NAME].parts['lower_02'].Surface(name='Surf-1', side2Edges=
    mdb.models[MODEL_NAME].parts['lower_02'].edges.getSequenceFromMask((
    '[#fffff ]', ), ))
mdb.models[MODEL_NAME].parts['lower_03'].Surface(name='Surf-1', side2Edges=
    mdb.models[MODEL_NAME].parts['lower_03'].edges.getSequenceFromMask((
    '[#1f ]', ), ))
mdb.models[MODEL_NAME].parts['lower_left_01'].Surface(name='Surf-1', 
    side2Edges=
    mdb.models[MODEL_NAME].parts['lower_left_01'].edges.getSequenceFromMask((
    '[#1f ]', ), ))
mdb.models[MODEL_NAME].parts['lower_right_01'].Surface(name='Surf-1', 
    side2Edges=
    mdb.models[MODEL_NAME].parts['lower_right_01'].edges.getSequenceFromMask((
    '[#1f ]', ), ))
mdb.models[MODEL_NAME].parts['pisador'].Surface(name='Surf-1', side2Edges=
    mdb.models[MODEL_NAME].parts['pisador'].edges.getSequenceFromMask(('[#1 ]', 
    ), ))
mdb.models[MODEL_NAME].parts['plate'].Surface(name='Surf-1', side1Edges=
    mdb.models[MODEL_NAME].parts['plate'].edges.getSequenceFromMask(('[#3d18 ]', 
    ), ))
mdb.models[MODEL_NAME].parts['upper_03'].Surface(name='Surf-1', side2Edges=
    mdb.models[MODEL_NAME].parts['upper_03'].edges.getSequenceFromMask((
    '[#1f ]', ), ))
mdb.models[MODEL_NAME].parts['upper_left_01'].Surface(name='Surf-1', 
    side2Edges=
    mdb.models[MODEL_NAME].parts['upper_left_01'].edges.getSequenceFromMask((
    '[#7 ]', ), ))
mdb.models[MODEL_NAME].parts['upper_left_02'].Surface(name='Surf-1', 
    side2Edges=
    mdb.models[MODEL_NAME].parts['upper_left_02'].edges.getSequenceFromMask((
    '[#3f ]', ), ))
mdb.models[MODEL_NAME].parts['upper_right_01'].Surface(name='Surf-1', 
    side2Edges=
    mdb.models[MODEL_NAME].parts['upper_right_01'].edges.getSequenceFromMask((
    '[#7 ]', ), ))
mdb.models[MODEL_NAME].parts['upper_right_02'].Surface(name='Surf-1', 
    side2Edges=
    mdb.models[MODEL_NAME].parts['upper_right_02'].edges.getSequenceFromMask((
    '[#3f ]', ), ))

# Create section  ===================================================================
mdb.models[MODEL_NAME].HomogeneousSolidSection(material='Acero 1018 US', name=
    'mp-section', thickness=2.99)
mdb.models[MODEL_NAME].parts['plate'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    faces=mdb.models[MODEL_NAME].parts['plate'].faces.getSequenceFromMask(
    mask=('[#1f ]', ), )), sectionName='mp-section', thicknessAssignment=
    FROM_SECTION)
	
# Inertia & Mass assignment ========================================================
mdb.models[MODEL_NAME].parts['lower_02'].engineeringFeatures.PointMassInertia(
    alpha=0.0, composite=0.0, i11=0.001, i22=0.001, i33=0.001, mass=0.01, name=
    'Inertia-1', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].parts['lower_02'].referencePoints[2], )))
mdb.models[MODEL_NAME].parts['lower_left_01'].engineeringFeatures.PointMassInertia(
    alpha=0.0, composite=0.0, i11=0.001, i22=0.001, i33=0.001, mass=0.01, name=
    'Inertia-1', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].parts['lower_left_01'].referencePoints[2], )))
mdb.models[MODEL_NAME].parts['lower_right_01'].engineeringFeatures.PointMassInertia(
    alpha=0.0, composite=0.0, i11=0.001, i22=0.001, i33=0.001, mass=0.01, name=
    'Inertia-1', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].parts['lower_right_01'].referencePoints[2], )))
mdb.models[MODEL_NAME].parts['pisador'].engineeringFeatures.PointMassInertia(
    alpha=0.0, composite=0.0, i11=0.001, i22=0.001, i33=0.001, mass=0.01, name=
    'Inertia-1', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].parts['pisador'].referencePoints[2], )))
	
# Regenerate assembly
mdb.models[MODEL_NAME].rootAssembly.regenerate()

# Constraints ========================================================================
mdb.models[MODEL_NAME].RigidBody(name='Constraint-1', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_02-1'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_02-1'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-2', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_02-2'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_02-2'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-3', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_03-1'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_03-1'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-4', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_left_01-1'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_left_01-1'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-5', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_left_01-2'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_left_01-2'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-6', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_right_01-1'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_right_01-1'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-7', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_right_01-2'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_right_01-2'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-8', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['pisador-1'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['pisador-1'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-9', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_03-1'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_03-1'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-10', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_left_01-1'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_left_01-1'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-11', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_left_02-1'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_left_02-1'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-12', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_right_01-1'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_right_01-1'].surfaces['Surf-1'])
mdb.models[MODEL_NAME].RigidBody(name='Constraint-13', refPointRegion=Region(
    referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_right_02-1'].referencePoints[2], 
    )), surfaceRegion=
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_right_02-1'].surfaces['Surf-1'])

# Contact properties
mdb.models[MODEL_NAME].ContactProperty('Friction')
mdb.models[MODEL_NAME].interactionProperties['Friction'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.1, ), ), temperatureDependency=OFF)

# Contacts =========================================================================
for _instance in mdb.models[MODEL_NAME].rootAssembly.instances.keys():
	if not(_instance=="plate-1"):
		mdb.models[MODEL_NAME].SurfaceToSurfaceContactExp(clearanceRegion=None, 
			createStepName=DYNEXP_STEPS[1], datumAxis=None, initialClearance=OMIT, 
			interactionProperty='Friction', master=
			mdb.models[MODEL_NAME].rootAssembly.instances[_instance].surfaces['Surf-1']
			, mechanicalConstraint=KINEMATIC, name="INT-"+_instance, slave=
			mdb.models[MODEL_NAME].rootAssembly.instances['plate-1'].surfaces['Surf-1']
			, sliding=FINITE)

mdb.models[MODEL_NAME].SelfContactExp(createStepName=DYNEXP_STEPS[1], 
    interactionProperty='Friction', mechanicalConstraint=KINEMATIC, name=
    'INT-SELF', surface=
    mdb.models[MODEL_NAME].rootAssembly.instances['plate-1'].surfaces['Surf-1'])

# mdb.models[MODEL_NAME].rootAssembly.regenerate()
mdb.models[MODEL_NAME].interactions['INT-lower_02-1'].move('Step-01-Down', 
    'Step-01-Up')
mdb.models[MODEL_NAME].interactions['INT-lower_02-1'].move('Step-01-Up', 
    'Step-02-Down')
mdb.models[MODEL_NAME].interactions['INT-lower_02-2'].deactivate('Step-02-Up')
mdb.models[MODEL_NAME].interactions['INT-lower_03-1'].move('Step-01-Down', 
    'Step-01-Up')
mdb.models[MODEL_NAME].interactions['INT-lower_03-1'].move('Step-01-Up', 
    'Step-02-Down')
mdb.models[MODEL_NAME].interactions['INT-lower_03-1'].move('Step-02-Down', 
    'Step-02-Up')
mdb.models[MODEL_NAME].interactions['INT-lower_03-1'].move('Step-02-Up', 
    'Step-03-Down')
mdb.models[MODEL_NAME].interactions['INT-lower_left_01-1'].deactivate(
    'Step-02-Down')
mdb.models[MODEL_NAME].interactions['INT-lower_left_01-2'].deactivate(
    'Step-02-Down')
mdb.models[MODEL_NAME].interactions['INT-lower_right_01-1'].deactivate(
    'Step-02-Down')
mdb.models[MODEL_NAME].interactions['INT-lower_right_01-2'].deactivate(
    'Step-02-Down')
mdb.models[MODEL_NAME].interactions['INT-pisador-1'].deactivate('Step-03-Down')
mdb.models[MODEL_NAME].interactions['INT-lower_02-1'].deactivate('Step-03-Down')
	
# Amplitude
mdb.models[MODEL_NAME].SmoothStepAmplitude(data=((0.0, 0.0), (0.86, 1.0)), 
    name='Amp-1', timeSpan=STEP)

# Field outputs
mdb.models['2D-MODEL'].fieldOutputRequests['F-Output-1'].setValues(
    exteriorOnly=OFF, rebar=EXCLUDE, region=MODEL, sectionPoints=DEFAULT, 
    timeInterval=TIME_PERIOD/NFRAMES, variables=PRESELECT)

	
# Boundary conditions  ====================================================================
# Fixed Points
mdb.models[MODEL_NAME].DisplacementBC(amplitude='Amp-1', createStepName=
    DYNEXP_STEPS[1], distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-Fixed-Points', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_02-2'].referencePoints[2], 
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_right_01-2'].referencePoints[2], 
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_left_01-2'].referencePoints[2], 
	mdb.models[MODEL_NAME].rootAssembly.instances['lower_03-1'].referencePoints[2],
    )), u1=0.0, u2=0, ur3=0.0)

# Upper
mdb.models[MODEL_NAME].DisplacementBC(amplitude='Amp-1', createStepName=
    DYNEXP_STEPS[1], distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-Upper-01', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_left_01-1'].referencePoints[2], 
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_right_01-1'].referencePoints[2], 
    )), u1=0.0, u2=-(YDISP), ur3=0.0)
	
mdb.models[MODEL_NAME].DisplacementBC(amplitude='Amp-1', createStepName=
    DYNEXP_STEPS[1], distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-Upper-02', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_left_02-1'].referencePoints[2], 
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_right_02-1'].referencePoints[2], 
    )), u1=0.0, u2=0, ur3=0.0)
	
mdb.models[MODEL_NAME].DisplacementBC(amplitude='Amp-1', createStepName=
    DYNEXP_STEPS[1], distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-Upper-03', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['upper_03-1'].referencePoints[2], ))
	, u1=0.0, u2=0, ur3=0.0)


mdb.models[MODEL_NAME].boundaryConditions['BC-Upper-01'].setValuesInStep(stepName=DYNEXP_STEPS[2], u2=YDISP)
mdb.models[MODEL_NAME].boundaryConditions['BC-Upper-01'].setValuesInStep(stepName=DYNEXP_STEPS[3], u2=0)

mdb.models[MODEL_NAME].boundaryConditions['BC-Upper-02'].setValuesInStep(stepName=DYNEXP_STEPS[3], u2=-(YDISP-0.006))
mdb.models[MODEL_NAME].boundaryConditions['BC-Upper-02'].setValuesInStep(stepName=DYNEXP_STEPS[4], u2=YDISP-0.006)
mdb.models[MODEL_NAME].boundaryConditions['BC-Upper-02'].setValuesInStep(stepName=DYNEXP_STEPS[5], u2=0)

mdb.models[MODEL_NAME].boundaryConditions['BC-Upper-03'].setValuesInStep(stepName=DYNEXP_STEPS[5], u2=-(YDISP+0.001))
mdb.models[MODEL_NAME].boundaryConditions['BC-Upper-03'].setValuesInStep(stepName=DYNEXP_STEPS[6], u2=(YDISP+0.001))

# Lower
mdb.models[MODEL_NAME].DisplacementBC(amplitude='Amp-1', createStepName=
    DYNEXP_STEPS[1], distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-LowerL-01', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_left_01-1'].referencePoints[2], 
    )), u1=0.0, u2=UNSET, ur3=0.0)
mdb.models[MODEL_NAME].DisplacementBC(amplitude='Amp-1', createStepName=
    DYNEXP_STEPS[1], distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-LowerR-01', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_right_01-1'].referencePoints[2], 
    )), u1=0.0, u2=UNSET, ur3=0.0)
	
mdb.models[MODEL_NAME].DisplacementBC(amplitude='Amp-1', createStepName=
    DYNEXP_STEPS[1], distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-Lower-02', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['lower_02-1'].referencePoints[2],  
    )), u1=0.0, u2=0.0, ur3=0.0)
	
mdb.models[MODEL_NAME].boundaryConditions['BC-LowerL-01'].setValuesInStep(stepName=DYNEXP_STEPS[2], u2=0.51)
mdb.models[MODEL_NAME].boundaryConditions['BC-LowerL-01'].setValuesInStep(stepName=DYNEXP_STEPS[3], u2=0.0)
mdb.models[MODEL_NAME].boundaryConditions['BC-LowerR-01'].setValuesInStep(stepName=DYNEXP_STEPS[2], u2=0.51)
mdb.models[MODEL_NAME].boundaryConditions['BC-LowerR-01'].setValuesInStep(stepName=DYNEXP_STEPS[3], u2=0.0)
mdb.models[MODEL_NAME].boundaryConditions['BC-Lower-02'].setValuesInStep(stepName=DYNEXP_STEPS[3], u2=FREED)
mdb.models[MODEL_NAME].boundaryConditions['BC-Lower-02'].setValuesInStep(stepName=DYNEXP_STEPS[4], u2=0.275)
mdb.models[MODEL_NAME].boundaryConditions['BC-Lower-02'].setValuesInStep(stepName=DYNEXP_STEPS[5], u2=0.0)

# Pisador
mdb.models[MODEL_NAME].DisplacementBC(amplitude='Amp-1', createStepName=
    DYNEXP_STEPS[1], distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-Pisador', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['pisador-1'].referencePoints[2],  
    )), u1=0.0, u2=UNSET, ur3=0.0)
mdb.models[MODEL_NAME].boundaryConditions['BC-Pisador'].setValuesInStep(stepName=DYNEXP_STEPS[5], u2=0.0)

# X-axis constrained
mdb.models[MODEL_NAME].DisplacementBC(amplitude=UNSET, createStepName=
    DYNEXP_STEPS[1], distributionType=UNIFORM, fieldName='', fixed=OFF, 
    localCsys=None, name='BC-8', region=Region(
    vertices=mdb.models[MODEL_NAME].rootAssembly.instances['plate-1'].vertices.getSequenceFromMask(
    mask=('[#2 ]', ), )), u1=0.0, u2=UNSET, ur3=UNSET)

# Loads  ===================================================================================
# Pisador 
mdb.models[MODEL_NAME].ConcentratedForce(amplitude='Amp-1', cf2=-2000.0, 
    createStepName=DYNEXP_STEPS[1], distributionType=UNIFORM, field='', 
    localCsys=None, name='Pisador-Force', region=Region(referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.instances['pisador-1'].referencePoints[2], 
    )))
mdb.models[MODEL_NAME].loads['Pisador-Force'].setValuesInStep(stepName=DYNEXP_STEPS[5], cf2=0.0)

# Botadores
mdb.models[MODEL_NAME].ConcentratedForce(amplitude='Amp-1', cf2=1000.0,
    createStepName=DYNEXP_STEPS[1], distributionType=UNIFORM, field='', 
    localCsys=None, name='B01L-Force', region=Region(referencePoints=(
	mdb.models[MODEL_NAME].rootAssembly.instances['lower_left_01-1'].referencePoints[2], 
    )))
mdb.models[MODEL_NAME].ConcentratedForce(amplitude='Amp-1', cf2=1000.0,
    createStepName=DYNEXP_STEPS[1], distributionType=UNIFORM, field='', 
    localCsys=None, name='B01R-Force', region=Region(referencePoints=(
	mdb.models[MODEL_NAME].rootAssembly.instances['lower_right_01-1'].referencePoints[2], 
    )))
mdb.models[MODEL_NAME].ConcentratedForce(amplitude='Amp-1', cf2=1999.5,
    createStepName=DYNEXP_STEPS[1], distributionType=UNIFORM, field='', 
    localCsys=None, name='B02-Force', region=Region(referencePoints=(
	mdb.models[MODEL_NAME].rootAssembly.instances['lower_02-1'].referencePoints[2],
    )))
mdb.models[MODEL_NAME].loads['B01L-Force'].setValuesInStep(stepName=DYNEXP_STEPS[2], cf2=0.0)
mdb.models[MODEL_NAME].loads['B01R-Force'].setValuesInStep(stepName=DYNEXP_STEPS[2], cf2=0.0)
mdb.models[MODEL_NAME].loads['B02-Force'].setValuesInStep(stepName=DYNEXP_STEPS[4], cf2=0.0)

# Gravity
mdb.models[MODEL_NAME].Gravity(amplitude='Amp-1', comp2=-386.0, createStepName=
    DYNEXP_STEPS[1], distributionType=UNIFORM, field='', name='Gravity', region=Region(
    faces=mdb.models[MODEL_NAME].rootAssembly.instances['plate-1'].faces.getSequenceFromMask(
    mask=('[#f ]', ), )))
	
# Mesh plate
mdb.models[MODEL_NAME].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=MESH_SIZE_QUAD)
mdb.models[MODEL_NAME].parts['plate'].seedEdgeBySize(constraint=FINER, 
    deviationFactor=0.1, edges=
    mdb.models[MODEL_NAME].parts['plate'].edges.getSequenceFromMask(('[#2100 ]', 
    ), ), minSizeFactor=0.1, size=MESH_SIZE_TRI)

mdb.models[MODEL_NAME].parts['plate'].setMeshControls(elemShape=TRI, regions=
    mdb.models[MODEL_NAME].parts['plate'].faces.getSequenceFromMask(('[#14 ]', 
    ), ))

mdb.models[MODEL_NAME].parts['plate'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4R, elemLibrary=EXPLICIT), ElemType(elemCode=CPE3, 
    elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, distortionControl=DEFAULT)), 
    regions=(mdb.models[MODEL_NAME].parts['plate'].faces.getSequenceFromMask((
    '[#14 ]', ), ), ))
mdb.models[MODEL_NAME].parts['plate'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, 
    hourglassControl=DEFAULT, distortionControl=DEFAULT), ElemType(
    elemCode=CPE3, elemLibrary=EXPLICIT)), regions=(
    mdb.models[MODEL_NAME].parts['plate'].faces.getSequenceFromMask(('[#b ]', 
    ), ), ))

mdb.models[MODEL_NAME].parts['plate'].generateMesh()

# Job
mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, 
    description='', echoPrint=OFF, explicitPrecision=SINGLE, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model=MODEL_NAME, modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name=JOB_NAME, nodalOutputPrecision=SINGLE, 
    numCpus=1, numDomains=1, parallelizationMethodExplicit=DOMAIN, queue=None, 
    resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=
    0, waitMinutes=0)
	
# mdb.jobs[JOB_NAME].submit(consistencyChecking=OFF)
