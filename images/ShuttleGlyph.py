try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

RenderView1 = CreateRenderView()
RenderView1.LightSpecularColor = [1.0, 1.0, 1.0]
RenderView1.UseOutlineForLODRendering = 0
RenderView1.KeyLightAzimuth = 10.0
RenderView1.UseTexturedBackground = 0
RenderView1.UseLight = 1
RenderView1.CameraPosition = [-0.436656408743753, 0.77204190707947995, 1.0467472730615099]
RenderView1.FillLightKFRatio = 3.0
RenderView1.Background2 = [0.0, 0.0, 0.16500000000000001]
RenderView1.FillLightAzimuth = -10.0
RenderView1.LODResolution = 0.5
RenderView1.BackgroundTexture = []
RenderView1.InteractionMode = '3D'
RenderView1.StencilCapable = 1
RenderView1.LightIntensity = 1.0
RenderView1.CameraFocalPoint = [3.45450344000764, -1.0314117267236, -0.38403729162136302]
RenderView1.ImageReductionFactor = 2
RenderView1.CameraViewAngle = 30.0
RenderView1.CameraParallelScale = 13.018103914927766
RenderView1.EyeAngle = 2.0
RenderView1.HeadLightKHRatio = 3.0
RenderView1.StereoRender = 0
RenderView1.KeyLightIntensity = 0.75
RenderView1.BackLightAzimuth = 110.0
RenderView1.OrientationAxesInteractivity = 0
RenderView1.UseInteractiveRenderingForSceenshots = 0
RenderView1.UseOffscreenRendering = 0
RenderView1.Background = [1.0, 1.0, 1.0]
RenderView1.UseOffscreenRenderingForScreenshots = 0
RenderView1.NonInteractiveRenderDelay = 0.0
RenderView1.CenterOfRotation = [1.43456923961639, 0.223376401700079, 0.55308338254690204]
RenderView1.CameraParallelProjection = 0
RenderView1.CompressorConfig = 'vtkSquirtCompressor 0 3'
RenderView1.HeadLightWarmth = 0.5
RenderView1.MaximumNumberOfPeels = 4
RenderView1.LightDiffuseColor = [1.0, 1.0, 1.0]
RenderView1.StereoType = 'Red-Blue'
RenderView1.DepthPeeling = 1
RenderView1.BackLightKBRatio = 3.5
RenderView1.StereoCapableWindow = 1
RenderView1.CameraViewUp = [0.27630197164006509, -0.15618419056013205, 0.94829516453838836]
RenderView1.LightType = 'HeadLight'
RenderView1.LightAmbientColor = [1.0, 1.0, 1.0]
RenderView1.RemoteRenderThreshold = 3.0
RenderView1.CacheKey = 0.0
RenderView1.UseCache = 0
RenderView1.KeyLightElevation = 50.0
RenderView1.CenterAxesVisibility = 0
RenderView1.MaintainLuminance = 0
RenderView1.StillRenderImageReductionFactor = 1
RenderView1.BackLightWarmth = 0.5
RenderView1.FillLightElevation = -75.0
RenderView1.MultiSamples = 0
RenderView1.FillLightWarmth = 0.40000000000000002
RenderView1.AlphaBitPlanes = 1
RenderView1.LightSwitch = 0
RenderView1.OrientationAxesVisibility = 0
RenderView1.CameraClippingRange = [0.018285832876048756, 18.285832876048755]
RenderView1.BackLightElevation = 0.0
RenderView1.ViewTime = 0.0
RenderView1.OrientationAxesOutlineColor = [1.0, 1.0, 1.0]
RenderView1.LODThreshold = 22.100000000000001
RenderView1.CollectGeometryThreshold = 100.0
RenderView1.UseGradientBackground = 0
RenderView1.KeyLightWarmth = 0.59999999999999998
RenderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]

shuttle_body_vtp = XMLPolyDataReader( guiName="shuttle_body.vtp", PointArrayStatus=['Momentum', 'Density', 'StagnationEnergy'], CellArrayStatus=[], FileName=['/Users/kmorel/data/sslv/body/shuttle_body.vtp'] )

Reflect1 = Reflect( guiName="Reflect1", CopyInput=1, Plane='Y', Center=0.0 )

Text1 = Text( guiName="Text1", Text='Glyph' )

sslv_pvd = PVDReader( guiName="sslv.pvd", FileName='/Users/kmorel/data/sslv/sslv.pvd' )

Glyph1 = Glyph( guiName="Glyph1", KeepRandomPoints=0, MaskPoints=1, RandomMode=1, Vectors=['POINTS', 'Momentum'], GlyphTransform="Transform2", GlyphType="Arrow", Scalars=['POINTS', 'Density'], ScaleMode='vector', MaximumNumberofPoints=5000, SetScaleFactor=0.050000000000000003, Orient=1 )
Glyph1.GlyphType.TipRadius = 0.10000000000000001
Glyph1.GlyphTransform.Rotate = [0.0, 0.0, 0.0]
Glyph1.GlyphType.TipLength = 0.34999999999999998
Glyph1.GlyphType.TipResolution = 6
Glyph1.GlyphTransform.Translate = [0.0, 0.0, 0.0]
Glyph1.GlyphType.ShaftRadius = 0.029999999999999999
Glyph1.GlyphTransform.Scale = [1.0, 1.0, 1.0]
Glyph1.GlyphType.Invert = 0
Glyph1.GlyphType.ShaftResolution = 6

a1_MomentumMagSqr_PiecewiseFunction = CreatePiecewiseFunction( Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0] )

a1_Density_PiecewiseFunction = CreatePiecewiseFunction( Points=[1.0, 0.0, 0.5, 0.0, 1.5, 1.0, 0.5, 0.0] )

a1_MomentumMagSqr_PVLookupTable = GetLookupTableForArray( "MomentumMagSqr", 1, Discretize=1, RGBPoints=[0.0, 0.23000000000000001, 0.29899999999999999, 0.754, 1.5624998328355399, 0.70599999999999996, 0.016, 0.14999999999999999], UseLogScale=0, VectorComponent=0, NanColor=[0.25, 0.0, 0.0], NumberOfTableValues=256, EnableOpacityMapping=0, ColorSpace='Diverging', IndexedLookup=0, VectorMode='Magnitude', ScalarOpacityFunction=a1_MomentumMagSqr_PiecewiseFunction, HSVWrap=0, ScalarRangeInitialized=1.0, AllowDuplicateScalars=1, Annotations=[], LockScalarRange=0 )

a1_Density_PVLookupTable = GetLookupTableForArray( "Density", 1, Discretize=1, RGBPoints=[1.0, 0.23000000000000001, 0.29899999999999999, 0.754, 1.5, 0.70599999999999996, 0.016, 0.14999999999999999], UseLogScale=0, VectorComponent=0, NanColor=[0.25, 0.0, 0.0], NumberOfTableValues=256, EnableOpacityMapping=0, ColorSpace='Diverging', IndexedLookup=0, VectorMode='Magnitude', ScalarOpacityFunction=a1_Density_PiecewiseFunction, HSVWrap=0, ScalarRangeInitialized=1.0, AllowDuplicateScalars=1, Annotations=[], LockScalarRange=1 )

SetActiveSource(shuttle_body_vtp)
DataRepresentation2 = Show()
DataRepresentation2.CubeAxesZAxisVisibility = 1
DataRepresentation2.SelectionPointLabelColor = [0.5, 0.5, 0.5]
DataRepresentation2.SelectionPointFieldDataArrayName = 'MomentumMagSqr'
DataRepresentation2.SuppressLOD = 0
DataRepresentation2.CubeAxesXGridLines = 0
DataRepresentation2.BlockVisibility = []
DataRepresentation2.CubeAxesYAxisTickVisibility = 1
DataRepresentation2.Position = [0.0, 0.0, 0.0]
DataRepresentation2.BackfaceRepresentation = 'Follow Frontface'
DataRepresentation2.SelectionOpacity = 1.0
DataRepresentation2.SelectionPointLabelShadow = 0
DataRepresentation2.CubeAxesYGridLines = 0
DataRepresentation2.CubeAxesZAxisTickVisibility = 1
DataRepresentation2.OrientationMode = 'Direction'
DataRepresentation2.ScaleMode = 'No Data Scaling Off'
DataRepresentation2.Diffuse = 1.0
DataRepresentation2.SelectionUseOutline = 0
DataRepresentation2.CubeAxesZTitle = 'Z-Axis'
DataRepresentation2.Specular = 0.10000000000000001
DataRepresentation2.SelectionVisibility = 1
DataRepresentation2.InterpolateScalarsBeforeMapping = 1
DataRepresentation2.CustomRangeActive = [0, 0, 0]
DataRepresentation2.Origin = [0.0, 0.0, 0.0]
DataRepresentation2.CubeAxesVisibility = 0
DataRepresentation2.Scale = [1.0, 1.0, 1.0]
DataRepresentation2.SelectionCellLabelJustification = 'Left'
DataRepresentation2.DiffuseColor = [1.0, 1.0, 1.0]
DataRepresentation2.SelectionCellLabelOpacity = 1.0
DataRepresentation2.Source = []
DataRepresentation2.Masking = 0
DataRepresentation2.Opacity = 1.0
DataRepresentation2.LineWidth = 1.0
DataRepresentation2.MeshVisibility = 0
DataRepresentation2.Visibility = 0
DataRepresentation2.SelectionCellLabelFontSize = 18
DataRepresentation2.CubeAxesCornerOffset = 0.0
DataRepresentation2.SelectionPointLabelJustification = 'Left'
DataRepresentation2.OriginalBoundsRangeActive = [0, 0, 0]
DataRepresentation2.SelectionPointLabelVisibility = 0
DataRepresentation2.SelectOrientationVectors = ''
DataRepresentation2.CubeAxesTickLocation = 'Inside'
DataRepresentation2.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
DataRepresentation2.CubeAxesYLabelFormat = '%-#6.3g'
DataRepresentation2.CubeAxesYAxisVisibility = 1
DataRepresentation2.SelectionPointLabelFontFamily = 'Arial'
DataRepresentation2.CubeAxesUseDefaultYTitle = 1
DataRepresentation2.SelectScaleArray = ''
DataRepresentation2.CubeAxesYTitle = 'Y-Axis'
DataRepresentation2.ColorAttributeType = 'POINT_DATA'
DataRepresentation2.AxesOrigin = [0.0, 0.0, 0.0]
DataRepresentation2.UserTransform = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
DataRepresentation2.SpecularPower = 100.0
DataRepresentation2.Texture = []
DataRepresentation2.SelectionCellLabelShadow = 0
DataRepresentation2.AmbientColor = [0.0, 0.0, 0.0]
DataRepresentation2.BlockOpacity = {}
DataRepresentation2.MapScalars = 1
DataRepresentation2.PointSize = 2.0
DataRepresentation2.CubeAxesUseDefaultXTitle = 1
DataRepresentation2.SelectionCellLabelFormat = ''
DataRepresentation2.Scaling = 0
DataRepresentation2.StaticMode = 0
DataRepresentation2.SelectionCellLabelColor = [0.0, 1.0, 0.0]
DataRepresentation2.EdgeColor = [0.0, 0.0, 0.50000762951094835]
DataRepresentation2.CubeAxesXAxisTickVisibility = 1
DataRepresentation2.SelectionCellLabelVisibility = 0
DataRepresentation2.NonlinearSubdivisionLevel = 1
DataRepresentation2.CubeAxesColor = [0.0, 0.0, 0.0]
DataRepresentation2.Representation = 'Surface'
DataRepresentation2.CustomRange = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
DataRepresentation2.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
DataRepresentation2.Orientation = [0.0, 0.0, 0.0]
DataRepresentation2.CubeAxesXTitle = 'X-Axis'
DataRepresentation2.CubeAxesInertia = 1
DataRepresentation2.BackfaceOpacity = 1.0
DataRepresentation2.SelectionPointLabelFontSize = 18
DataRepresentation2.SelectionCellFieldDataArrayName = 'vtkOriginalCellIds'
DataRepresentation2.SelectionColor = [1.0, 0.0, 1.0]
DataRepresentation2.BlockColor = {}
DataRepresentation2.Ambient = 0.0
DataRepresentation2.CubeAxesXAxisMinorTickVisibility = 1
DataRepresentation2.ScaleFactor = 0.21960260868072501
DataRepresentation2.BackfaceAmbientColor = [1.0, 1.0, 1.0]
DataRepresentation2.SelectMaskArray = ''
DataRepresentation2.SelectionLineWidth = 2.0
DataRepresentation2.CubeAxesZAxisMinorTickVisibility = 1
DataRepresentation2.CubeAxesXAxisVisibility = 1
DataRepresentation2.CubeAxesXLabelFormat = '%-#6.3g'
DataRepresentation2.Interpolation = 'Gouraud'
DataRepresentation2.CubeAxesZLabelFormat = '%-#6.3g'
DataRepresentation2.SelectionCellLabelFontFamily = 'Arial'
DataRepresentation2.SelectionCellLabelItalic = 0
DataRepresentation2.CubeAxesYAxisMinorTickVisibility = 1
DataRepresentation2.CubeAxesZGridLines = 0
DataRepresentation2.SelectionPointLabelFormat = ''
DataRepresentation2.SelectionPointLabelOpacity = 1.0
DataRepresentation2.UseAxesOrigin = 0
DataRepresentation2.CubeAxesFlyMode = 'Closest Triad'
DataRepresentation2.Pickable = 1
DataRepresentation2.CustomBoundsActive = [0, 0, 0]
DataRepresentation2.CubeAxesGridLineLocation = 'All Faces'
DataRepresentation2.SelectionRepresentation = 'Wireframe'
DataRepresentation2.SelectionPointLabelBold = 0
DataRepresentation2.ColorArrayName = ('POINT_DATA', 'MomentumMagSqr')
DataRepresentation2.SelectionPointLabelItalic = 0
DataRepresentation2.AllowSpecularHighlightingWithScalarColoring = 0
DataRepresentation2.SpecularColor = [1.0, 1.0, 1.0]
DataRepresentation2.CubeAxesUseDefaultZTitle = 1
DataRepresentation2.LookupTable = a1_MomentumMagSqr_PVLookupTable
DataRepresentation2.SelectionPointSize = 5.0
DataRepresentation2.SelectionCellLabelBold = 0
DataRepresentation2.Orient = 0

SetActiveSource(Reflect1)
DataRepresentation4 = Show()
DataRepresentation4.CubeAxesZAxisVisibility = 1
DataRepresentation4.SelectionPointLabelColor = [0.5, 0.5, 0.5]
DataRepresentation4.SelectionPointFieldDataArrayName = 'Density'
DataRepresentation4.SuppressLOD = 0
DataRepresentation4.CubeAxesXGridLines = 0
DataRepresentation4.BlockVisibility = []
DataRepresentation4.CubeAxesYAxisTickVisibility = 1
DataRepresentation4.Position = [0.0, 0.0, 0.0]
DataRepresentation4.BackfaceRepresentation = 'Follow Frontface'
DataRepresentation4.SelectionOpacity = 1.0
DataRepresentation4.SelectionPointLabelShadow = 0
DataRepresentation4.CubeAxesYGridLines = 0
DataRepresentation4.CubeAxesZAxisTickVisibility = 1
DataRepresentation4.OrientationMode = 'Direction'
DataRepresentation4.ScaleMode = 'No Data Scaling Off'
DataRepresentation4.Diffuse = 1.0
DataRepresentation4.SelectionUseOutline = 0
DataRepresentation4.SelectionPointLabelFormat = ''
DataRepresentation4.CubeAxesZTitle = 'Z-Axis'
DataRepresentation4.Specular = 0.10000000000000001
DataRepresentation4.SelectionVisibility = 1
DataRepresentation4.InterpolateScalarsBeforeMapping = 1
DataRepresentation4.CustomRangeActive = [0, 0, 0]
DataRepresentation4.Origin = [0.0, 0.0, 0.0]
DataRepresentation4.CubeAxesVisibility = 0
DataRepresentation4.Scale = [1.0, 1.0, 1.0]
DataRepresentation4.SelectionCellLabelJustification = 'Left'
DataRepresentation4.DiffuseColor = [1.0, 1.0, 1.0]
DataRepresentation4.SelectionCellLabelOpacity = 1.0
DataRepresentation4.CubeAxesInertia = 1
DataRepresentation4.Source = []
DataRepresentation4.Masking = 0
DataRepresentation4.Opacity = 1.0
DataRepresentation4.LineWidth = 1.0
DataRepresentation4.MeshVisibility = 0
DataRepresentation4.Visibility = 1
DataRepresentation4.SelectionCellLabelFontSize = 18
DataRepresentation4.CubeAxesCornerOffset = 0.0
DataRepresentation4.SelectionPointLabelJustification = 'Left'
DataRepresentation4.OriginalBoundsRangeActive = [0, 0, 0]
DataRepresentation4.SelectionPointLabelVisibility = 0
DataRepresentation4.SelectOrientationVectors = ''
DataRepresentation4.CubeAxesTickLocation = 'Inside'
DataRepresentation4.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
DataRepresentation4.CubeAxesYLabelFormat = '%-#6.3g'
DataRepresentation4.CubeAxesYAxisVisibility = 1
DataRepresentation4.SelectionPointLabelFontFamily = 'Arial'
DataRepresentation4.CubeAxesUseDefaultYTitle = 1
DataRepresentation4.SelectScaleArray = ''
DataRepresentation4.CubeAxesYTitle = 'Y-Axis'
DataRepresentation4.ColorAttributeType = 'POINT_DATA'
DataRepresentation4.AxesOrigin = [0.0, 0.0, 0.0]
DataRepresentation4.UserTransform = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
DataRepresentation4.SpecularPower = 100.0
DataRepresentation4.Texture = []
DataRepresentation4.SelectionCellLabelShadow = 0
DataRepresentation4.AmbientColor = [0.0, 0.0, 0.0]
DataRepresentation4.BlockOpacity = {}
DataRepresentation4.MapScalars = 1
DataRepresentation4.PointSize = 2.0
DataRepresentation4.CubeAxesUseDefaultXTitle = 1
DataRepresentation4.SelectionCellLabelFormat = ''
DataRepresentation4.Scaling = 0
DataRepresentation4.StaticMode = 0
DataRepresentation4.SelectionCellLabelColor = [0.0, 1.0, 0.0]
DataRepresentation4.EdgeColor = [0.0, 0.0, 0.50000762951094835]
DataRepresentation4.CubeAxesXAxisTickVisibility = 1
DataRepresentation4.SelectionCellLabelVisibility = 0
DataRepresentation4.NonlinearSubdivisionLevel = 1
DataRepresentation4.CubeAxesColor = [0.0, 0.0, 0.0]
DataRepresentation4.Representation = 'Surface'
DataRepresentation4.CustomRange = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
DataRepresentation4.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
DataRepresentation4.Orientation = [0.0, 0.0, 0.0]
DataRepresentation4.CubeAxesXTitle = 'X-Axis'
DataRepresentation4.ScalarOpacityUnitDistance = 0.044217716343397002
DataRepresentation4.BackfaceOpacity = 1.0
DataRepresentation4.SelectionPointLabelFontSize = 18
DataRepresentation4.SelectionCellFieldDataArrayName = 'vtkOriginalCellIds'
DataRepresentation4.SelectionColor = [1.0, 0.0, 1.0]
DataRepresentation4.BlockColor = {}
DataRepresentation4.Ambient = 0.0
DataRepresentation4.CubeAxesXAxisMinorTickVisibility = 1
DataRepresentation4.ScaleFactor = 0.21960260868072501
DataRepresentation4.BackfaceAmbientColor = [1.0, 1.0, 1.0]
DataRepresentation4.ScalarOpacityFunction = []
DataRepresentation4.SelectMaskArray = ''
DataRepresentation4.SelectionLineWidth = 2.0
DataRepresentation4.CubeAxesZAxisMinorTickVisibility = 1
DataRepresentation4.CubeAxesXAxisVisibility = 1
DataRepresentation4.CubeAxesXLabelFormat = '%-#6.3g'
DataRepresentation4.Interpolation = 'Gouraud'
DataRepresentation4.CubeAxesZLabelFormat = '%-#6.3g'
DataRepresentation4.SelectMapper = 'Projected tetra'
DataRepresentation4.SelectionCellLabelFontFamily = 'Arial'
DataRepresentation4.SelectionCellLabelItalic = 0
DataRepresentation4.CubeAxesYAxisMinorTickVisibility = 1
DataRepresentation4.CubeAxesZGridLines = 0
DataRepresentation4.ExtractedBlockIndex = 0
DataRepresentation4.SelectionPointLabelOpacity = 1.0
DataRepresentation4.UseAxesOrigin = 0
DataRepresentation4.CubeAxesFlyMode = 'Closest Triad'
DataRepresentation4.Pickable = 1
DataRepresentation4.CustomBoundsActive = [0, 0, 0]
DataRepresentation4.CubeAxesGridLineLocation = 'All Faces'
DataRepresentation4.SelectionRepresentation = 'Wireframe'
DataRepresentation4.SelectionPointLabelBold = 0
DataRepresentation4.ColorArrayName = ('POINT_DATA', '')
DataRepresentation4.SelectionPointLabelItalic = 0
DataRepresentation4.AllowSpecularHighlightingWithScalarColoring = 0
DataRepresentation4.SpecularColor = [1.0, 1.0, 1.0]
DataRepresentation4.CubeAxesUseDefaultZTitle = 1
DataRepresentation4.LookupTable = []
DataRepresentation4.SelectionPointSize = 5.0
DataRepresentation4.SelectionCellLabelBold = 0
DataRepresentation4.Orient = 0

SetActiveSource(Text1)
DataRepresentation5 = Show()
DataRepresentation5.Interactivity = 1
DataRepresentation5.Opacity = 1.0
DataRepresentation5.Justification = 'Left'
DataRepresentation5.Bold = 0
DataRepresentation5.Resizable = 0
DataRepresentation5.Color = [0.0, 0.0, 0.0]
DataRepresentation5.WindowLocation = 'AnyLocation'
DataRepresentation5.TextScaleMode = 'Viewport'
DataRepresentation5.Visibility = 1
DataRepresentation5.FontFamily = 'Times'
DataRepresentation5.FontSize = 24
DataRepresentation5.Italic = 0
DataRepresentation5.Position = [0.050000000000000003, 0.050000000000000003]
DataRepresentation5.Shadow = 0
DataRepresentation5.Position2 = [0.10000000000000001, 0.10000000000000001]
DataRepresentation5.Orientation = 0.0

SetActiveSource(sslv_pvd)
DataRepresentation1 = Show()
DataRepresentation1.CubeAxesZAxisVisibility = 1
DataRepresentation1.SelectionPointLabelColor = [0.5, 0.5, 0.5]
DataRepresentation1.SelectionPointFieldDataArrayName = 'Density'
DataRepresentation1.SuppressLOD = 0
DataRepresentation1.CubeAxesXGridLines = 0
DataRepresentation1.BlockVisibility = []
DataRepresentation1.CubeAxesYAxisTickVisibility = 1
DataRepresentation1.Position = [0.0, 0.0, 0.0]
DataRepresentation1.BackfaceRepresentation = 'Follow Frontface'
DataRepresentation1.SelectionOpacity = 1.0
DataRepresentation1.SelectionPointLabelShadow = 0
DataRepresentation1.CubeAxesYGridLines = 0
DataRepresentation1.CubeAxesZAxisTickVisibility = 1
DataRepresentation1.OrientationMode = 'Direction'
DataRepresentation1.ScaleMode = 'No Data Scaling Off'
DataRepresentation1.Diffuse = 1.0
DataRepresentation1.SelectionUseOutline = 0
DataRepresentation1.SelectionPointLabelFormat = ''
DataRepresentation1.CubeAxesZTitle = 'Z-Axis'
DataRepresentation1.Specular = 0.10000000000000001
DataRepresentation1.SelectionVisibility = 1
DataRepresentation1.InterpolateScalarsBeforeMapping = 1
DataRepresentation1.CustomRangeActive = [0, 0, 0]
DataRepresentation1.Origin = [0.0, 0.0, 0.0]
DataRepresentation1.CubeAxesVisibility = 0
DataRepresentation1.Scale = [1.0, 1.0, 1.0]
DataRepresentation1.SelectionCellLabelJustification = 'Left'
DataRepresentation1.DiffuseColor = [1.0, 1.0, 1.0]
DataRepresentation1.SelectionCellLabelOpacity = 1.0
DataRepresentation1.CubeAxesInertia = 1
DataRepresentation1.Source = []
DataRepresentation1.Masking = 0
DataRepresentation1.Opacity = 1.0
DataRepresentation1.LineWidth = 1.0
DataRepresentation1.MeshVisibility = 0
DataRepresentation1.Visibility = 0
DataRepresentation1.SelectionCellLabelFontSize = 18
DataRepresentation1.CubeAxesCornerOffset = 0.0
DataRepresentation1.SelectionPointLabelJustification = 'Left'
DataRepresentation1.OriginalBoundsRangeActive = [0, 0, 0]
DataRepresentation1.SelectionPointLabelVisibility = 0
DataRepresentation1.SelectOrientationVectors = ''
DataRepresentation1.CubeAxesTickLocation = 'Inside'
DataRepresentation1.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
DataRepresentation1.CubeAxesYLabelFormat = '%-#6.3g'
DataRepresentation1.CubeAxesYAxisVisibility = 1
DataRepresentation1.SelectionPointLabelFontFamily = 'Arial'
DataRepresentation1.CubeAxesUseDefaultYTitle = 1
DataRepresentation1.SelectScaleArray = ''
DataRepresentation1.CubeAxesYTitle = 'Y-Axis'
DataRepresentation1.ColorAttributeType = 'POINT_DATA'
DataRepresentation1.AxesOrigin = [0.0, 0.0, 0.0]
DataRepresentation1.UserTransform = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
DataRepresentation1.SpecularPower = 100.0
DataRepresentation1.Texture = []
DataRepresentation1.SelectionCellLabelShadow = 0
DataRepresentation1.AmbientColor = [0.0, 0.0, 0.0]
DataRepresentation1.BlockOpacity = {}
DataRepresentation1.MapScalars = 1
DataRepresentation1.PointSize = 2.0
DataRepresentation1.CubeAxesUseDefaultXTitle = 1
DataRepresentation1.SelectionCellLabelFormat = ''
DataRepresentation1.Scaling = 0
DataRepresentation1.StaticMode = 0
DataRepresentation1.SelectionCellLabelColor = [0.0, 1.0, 0.0]
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.50000762951094835]
DataRepresentation1.CubeAxesXAxisTickVisibility = 1
DataRepresentation1.UseDataParititions = 1
DataRepresentation1.SelectionCellLabelVisibility = 0
DataRepresentation1.NonlinearSubdivisionLevel = 1
DataRepresentation1.CubeAxesColor = [0.0, 0.0, 0.0]
DataRepresentation1.Representation = 'Outline'
DataRepresentation1.CustomRange = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
DataRepresentation1.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
DataRepresentation1.Orientation = [0.0, 0.0, 0.0]
DataRepresentation1.CubeAxesXTitle = 'X-Axis'
DataRepresentation1.ScalarOpacityUnitDistance = 0.22589562046819894
DataRepresentation1.BackfaceOpacity = 1.0
DataRepresentation1.SelectionPointLabelFontSize = 18
DataRepresentation1.SelectionCellFieldDataArrayName = 'vtkOriginalCellIds'
DataRepresentation1.SelectionColor = [1.0, 0.0, 1.0]
DataRepresentation1.BlockColor = {}
DataRepresentation1.Ambient = 0.0
DataRepresentation1.CubeAxesXAxisMinorTickVisibility = 1
DataRepresentation1.ScaleFactor = 1.4668267250061036
DataRepresentation1.BackfaceAmbientColor = [1.0, 1.0, 1.0]
DataRepresentation1.ScalarOpacityFunction = []
DataRepresentation1.SelectMaskArray = ''
DataRepresentation1.SelectionLineWidth = 2.0
DataRepresentation1.CubeAxesZAxisMinorTickVisibility = 1
DataRepresentation1.CubeAxesXAxisVisibility = 1
DataRepresentation1.CubeAxesXLabelFormat = '%-#6.3g'
DataRepresentation1.Interpolation = 'Gouraud'
DataRepresentation1.CubeAxesZLabelFormat = '%-#6.3g'
DataRepresentation1.SelectMapper = 'Projected tetra'
DataRepresentation1.SelectionCellLabelFontFamily = 'Arial'
DataRepresentation1.SelectionCellLabelItalic = 0
DataRepresentation1.CubeAxesYAxisMinorTickVisibility = 1
DataRepresentation1.CubeAxesZGridLines = 0
DataRepresentation1.ExtractedBlockIndex = 2
DataRepresentation1.SelectionPointLabelOpacity = 1.0
DataRepresentation1.UseAxesOrigin = 0
DataRepresentation1.CubeAxesFlyMode = 'Closest Triad'
DataRepresentation1.Pickable = 1
DataRepresentation1.CustomBoundsActive = [0, 0, 0]
DataRepresentation1.CubeAxesGridLineLocation = 'All Faces'
DataRepresentation1.SelectionRepresentation = 'Wireframe'
DataRepresentation1.SelectionPointLabelBold = 0
DataRepresentation1.ColorArrayName = ('POINT_DATA', '')
DataRepresentation1.SelectionPointLabelItalic = 0
DataRepresentation1.AllowSpecularHighlightingWithScalarColoring = 0
DataRepresentation1.SpecularColor = [1.0, 1.0, 1.0]
DataRepresentation1.CubeAxesUseDefaultZTitle = 1
DataRepresentation1.LookupTable = []
DataRepresentation1.SelectionPointSize = 5.0
DataRepresentation1.SelectionCellLabelBold = 0
DataRepresentation1.Orient = 0

SetActiveSource(Glyph1)
DataRepresentation4 = Show()
DataRepresentation4.CubeAxesZAxisVisibility = 1
DataRepresentation4.SelectionPointLabelColor = [0.5, 0.5, 0.5]
DataRepresentation4.SelectionPointFieldDataArrayName = 'Density'
DataRepresentation4.SuppressLOD = 0
DataRepresentation4.CubeAxesXGridLines = 0
DataRepresentation4.BlockVisibility = []
DataRepresentation4.CubeAxesYAxisTickVisibility = 1
DataRepresentation4.Position = [0.0, 0.0, 0.0]
DataRepresentation4.BackfaceRepresentation = 'Follow Frontface'
DataRepresentation4.SelectionOpacity = 1.0
DataRepresentation4.SelectionPointLabelShadow = 0
DataRepresentation4.CubeAxesYGridLines = 0
DataRepresentation4.CubeAxesZAxisTickVisibility = 1
DataRepresentation4.OrientationMode = 'Direction'
DataRepresentation4.ScaleMode = 'No Data Scaling Off'
DataRepresentation4.Diffuse = 1.0
DataRepresentation4.SelectionUseOutline = 0
DataRepresentation4.CubeAxesZTitle = 'Z-Axis'
DataRepresentation4.Specular = 0.10000000000000001
DataRepresentation4.SelectionVisibility = 1
DataRepresentation4.InterpolateScalarsBeforeMapping = 1
DataRepresentation4.CustomRangeActive = [0, 0, 0]
DataRepresentation4.Origin = [0.0, 0.0, 0.0]
DataRepresentation4.CubeAxesVisibility = 0
DataRepresentation4.Scale = [1.0, 1.0, 1.0]
DataRepresentation4.SelectionCellLabelJustification = 'Left'
DataRepresentation4.DiffuseColor = [0.28152895399404898, 0.90176241702906845, 0.0]
DataRepresentation4.SelectionCellLabelOpacity = 1.0
DataRepresentation4.Source = []
DataRepresentation4.Masking = 0
DataRepresentation4.Opacity = 1.0
DataRepresentation4.LineWidth = 1.0
DataRepresentation4.MeshVisibility = 0
DataRepresentation4.Visibility = 1
DataRepresentation4.SelectionCellLabelFontSize = 18
DataRepresentation4.CubeAxesCornerOffset = 0.0
DataRepresentation4.SelectionPointLabelJustification = 'Left'
DataRepresentation4.OriginalBoundsRangeActive = [0, 0, 0]
DataRepresentation4.SelectionPointLabelVisibility = 0
DataRepresentation4.SelectOrientationVectors = ''
DataRepresentation4.CubeAxesTickLocation = 'Inside'
DataRepresentation4.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
DataRepresentation4.CubeAxesYLabelFormat = '%-#6.3g'
DataRepresentation4.CubeAxesYAxisVisibility = 1
DataRepresentation4.SelectionPointLabelFontFamily = 'Arial'
DataRepresentation4.CubeAxesUseDefaultYTitle = 1
DataRepresentation4.SelectScaleArray = ''
DataRepresentation4.CubeAxesYTitle = 'Y-Axis'
DataRepresentation4.ColorAttributeType = 'POINT_DATA'
DataRepresentation4.AxesOrigin = [0.0, 0.0, 0.0]
DataRepresentation4.UserTransform = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
DataRepresentation4.SpecularPower = 100.0
DataRepresentation4.Texture = []
DataRepresentation4.SelectionCellLabelShadow = 0
DataRepresentation4.AmbientColor = [0.0, 0.0, 0.0]
DataRepresentation4.BlockOpacity = {}
DataRepresentation4.MapScalars = 1
DataRepresentation4.PointSize = 2.0
DataRepresentation4.CubeAxesUseDefaultXTitle = 1
DataRepresentation4.SelectionCellLabelFormat = ''
DataRepresentation4.Scaling = 0
DataRepresentation4.StaticMode = 0
DataRepresentation4.SelectionCellLabelColor = [0.0, 1.0, 0.0]
DataRepresentation4.EdgeColor = [0.0, 0.0, 0.50000762951094835]
DataRepresentation4.CubeAxesXAxisTickVisibility = 1
DataRepresentation4.SelectionCellLabelVisibility = 0
DataRepresentation4.NonlinearSubdivisionLevel = 1
DataRepresentation4.CubeAxesColor = [0.0, 0.0, 0.0]
DataRepresentation4.Representation = 'Surface'
DataRepresentation4.CustomRange = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
DataRepresentation4.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
DataRepresentation4.Orientation = [0.0, 0.0, 0.0]
DataRepresentation4.CubeAxesXTitle = 'X-Axis'
DataRepresentation4.CubeAxesInertia = 1
DataRepresentation4.BackfaceOpacity = 1.0
DataRepresentation4.SelectionPointLabelFontSize = 18
DataRepresentation4.SelectionCellFieldDataArrayName = 'vtkOriginalCellIds'
DataRepresentation4.SelectionColor = [1.0, 0.0, 1.0]
DataRepresentation4.BlockColor = {}
DataRepresentation4.Ambient = 0.0
DataRepresentation4.CubeAxesXAxisMinorTickVisibility = 1
DataRepresentation4.ScaleFactor = 1.509355115890503
DataRepresentation4.BackfaceAmbientColor = [1.0, 1.0, 1.0]
DataRepresentation4.SelectMaskArray = ''
DataRepresentation4.SelectionLineWidth = 2.0
DataRepresentation4.CubeAxesZAxisMinorTickVisibility = 1
DataRepresentation4.CubeAxesXAxisVisibility = 1
DataRepresentation4.CubeAxesXLabelFormat = '%-#6.3g'
DataRepresentation4.Interpolation = 'Gouraud'
DataRepresentation4.CubeAxesZLabelFormat = '%-#6.3g'
DataRepresentation4.SelectionCellLabelFontFamily = 'Arial'
DataRepresentation4.SelectionCellLabelItalic = 0
DataRepresentation4.CubeAxesYAxisMinorTickVisibility = 1
DataRepresentation4.CubeAxesZGridLines = 0
DataRepresentation4.SelectionPointLabelFormat = ''
DataRepresentation4.SelectionPointLabelOpacity = 1.0
DataRepresentation4.UseAxesOrigin = 0
DataRepresentation4.CubeAxesFlyMode = 'Closest Triad'
DataRepresentation4.Pickable = 1
DataRepresentation4.CustomBoundsActive = [0, 0, 0]
DataRepresentation4.CubeAxesGridLineLocation = 'All Faces'
DataRepresentation4.SelectionRepresentation = 'Wireframe'
DataRepresentation4.SelectionPointLabelBold = 0
DataRepresentation4.ColorArrayName = ('POINT_DATA', '')
DataRepresentation4.SelectionPointLabelItalic = 0
DataRepresentation4.AllowSpecularHighlightingWithScalarColoring = 0
DataRepresentation4.SpecularColor = [1.0, 1.0, 1.0]
DataRepresentation4.CubeAxesUseDefaultZTitle = 1
DataRepresentation4.LookupTable = a1_Density_PVLookupTable
DataRepresentation4.SelectionPointSize = 5.0
DataRepresentation4.SelectionCellLabelBold = 0
DataRepresentation4.Orient = 0

Render()
