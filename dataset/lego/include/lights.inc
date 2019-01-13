// radiosity (global illumination) settings
#default{ finish{ ambient 0 diffuse 1 }} 

global_settings {
  radiosity {
    pretrace_start 0.08           // start pretrace at this size
    pretrace_end   0.04           // end pretrace at this size
    count 35                      // higher -> higher quality (1..1600) [35]

    nearest_count 5               // higher -> higher quality (1..10) [5]
    error_bound 1.8               // higher -> smoother, less accurate [1.8]
    recursion_limit 3             // how much interreflections are calculated (1..5+) [3]

    low_error_factor .5           // reduce error_bound during last pretrace step
    gray_threshold 0.0            // increase for weakening colors (0..1) [0]
    minimum_reuse 0.015           // reuse of old radiosity samples [0.015]
    brightness 1                  // brightness of radiosity effects (0..1) [1]

    adc_bailout 0.01/2
    //normal on                   // take surface normals into account [off]
    //media on                    // take media into account [off]
    //save_file "file_name"       // save radiosity data
    //load_file "file_name"       // load saved radiosity data
    //always_sample off           // turn sampling in final trace off [on]
    //max_sample 1.0              // maximum brightness of samples
  }
}

#declare GD_LightPointsX = 8;
#declare GD_LightPointsY = 8;

//#declare GD_SkipAreaLight = 0;

#ifndef (LDXSkipLight1)
light_source {  // Latitude,Longitude: 45,0,LDXRadius*2
    <0*LDXRadius,-1.414214*LDXRadius,-1.414214*LDXRadius> + LDXCenter
    color rgb <1,1,1>
    #ifndef (GD_SkipAreaLight)
        area_light 200, 200, GD_LightPointsX, GD_LightPointsY
        jitter
    #end
}
#end
#ifndef (LDXSkipLight2)
light_source {  // Latitude,Longitude: 30,120,LDXRadius*2
    <1.5*LDXRadius,-1*LDXRadius,0.866026*LDXRadius> + LDXCenter
    color rgb <1,1,1>
    #ifndef (GD_SkipAreaLight)
        area_light 200, 200, GD_LightPointsX, GD_LightPointsY
        jitter
    #end
}
#end
#ifndef (LDXSkipLight3)
light_source {  // Latitude,Longitude: 60,-120,LDXRadius*2
    <-0.866025*LDXRadius,-1.732051*LDXRadius,0.5*LDXRadius> + LDXCenter
    color rgb <1,1,1>
    #ifndef (GD_SkipAreaLight)
        area_light 200, 200, GD_LightPointsX, GD_LightPointsY
        jitter
    #end
}
#end
