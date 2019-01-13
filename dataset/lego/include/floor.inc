object {
    plane { LDXFloorAxis, LDXFloorLoc hollow }
    texture {
        pigment
        {
            image_map
            {
                jpeg "grey-felt-texture.jpg"

            }
        }
        finish { ambient LDXFloorAmb diffuse LDXFloorDif }
    }
}