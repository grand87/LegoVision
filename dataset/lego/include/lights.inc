#declare GD_LightPointsX = 8;
#declare GD_LightPointsY = 8;

#declare GD_SkipAreaLight = 1;

#ifndef (LDXSkipLight1)
light_source {	// Latitude,Longitude: 45,0,LDXRadius*2
	<0*LDXRadius,-1.414214*LDXRadius,-1.414214*LDXRadius> + LDXCenter
	color rgb <1,1,1>
	#ifndef (GD_SkipAreaLight)
    	area_light 200, 200, GD_LightPointsX, GD_LightPointsY
    	jitter
	#end	
}
#end
#ifndef (LDXSkipLight2)
light_source {	// Latitude,Longitude: 30,120,LDXRadius*2
	<1.5*LDXRadius,-1*LDXRadius,0.866026*LDXRadius> + LDXCenter
	color rgb <1,1,1>
	#ifndef (GD_SkipAreaLight)
    	area_light 200, 200, GD_LightPointsX, GD_LightPointsY
    	jitter
	#end	
}
#end
#ifndef (LDXSkipLight3)
light_source {	// Latitude,Longitude: 60,-120,LDXRadius*2
	<-0.866025*LDXRadius,-1.732051*LDXRadius,0.5*LDXRadius> + LDXCenter
	color rgb <1,1,1>
	#ifndef (GD_SkipAreaLight)
    	area_light 200, 200, GD_LightPointsX, GD_LightPointsY
    	jitter
	#end	
}
#end
