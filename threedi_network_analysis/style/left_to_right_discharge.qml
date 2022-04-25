<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="Symbology" version="3.22.3-Białowieża">
  <renderer-v2 symbollevels="0" enableorderby="0" referencescale="-1" forceraster="0" type="singleSymbol">
    <symbols>
      <symbol clip_to_extent="1" name="0" type="line" alpha="1" force_rhr="0">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" class="GeometryGenerator" enabled="1" locked="0">
          <Option type="Map">
            <Option value="Line" name="SymbolType" type="QString"/>
            <Option value="make_line( &#xd;&#xa;&#x9;line_interpolate_point( &#xd;&#xa;&#x9;&#x9;$geometry, &#xd;&#xa;&#x9;&#x9;0.5*$length&#xd;&#xa;&#x9;),&#xd;&#xa;&#x9;line_interpolate_point( &#xd;&#xa;&#x9;&#x9; offset_curve( $geometry, 100), &#xd;&#xa;&#x9;&#x9;0.5*length(offset_curve( $geometry, 100) )&#xd;&#xa;&#x9;)&#xd;&#xa;)" name="geometryModifier" type="QString"/>
            <Option value="MapUnit" name="units" type="QString"/>
          </Option>
          <prop v="Line" k="SymbolType"/>
          <prop v="make_line( &#xd;&#xa;&#x9;line_interpolate_point( &#xd;&#xa;&#x9;&#x9;$geometry, &#xd;&#xa;&#x9;&#x9;0.5*$length&#xd;&#xa;&#x9;),&#xd;&#xa;&#x9;line_interpolate_point( &#xd;&#xa;&#x9;&#x9; offset_curve( $geometry, 100), &#xd;&#xa;&#x9;&#x9;0.5*length(offset_curve( $geometry, 100) )&#xd;&#xa;&#x9;)&#xd;&#xa;)" k="geometryModifier"/>
          <prop v="MapUnit" k="units"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@0@0" type="line" alpha="1" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer pass="0" class="ArrowLine" enabled="1" locked="0">
              <Option type="Map">
                <Option value="4" name="arrow_start_width" type="QString"/>
                <Option value="MM" name="arrow_start_width_unit" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="arrow_start_width_unit_scale" type="QString"/>
                <Option value="0" name="arrow_type" type="QString"/>
                <Option value="1.8" name="arrow_width" type="QString"/>
                <Option value="MM" name="arrow_width_unit" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="arrow_width_unit_scale" type="QString"/>
                <Option value="3.9" name="head_length" type="QString"/>
                <Option value="MM" name="head_length_unit" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="head_length_unit_scale" type="QString"/>
                <Option value="2.9" name="head_thickness" type="QString"/>
                <Option value="MM" name="head_thickness_unit" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="head_thickness_unit_scale" type="QString"/>
                <Option value="0" name="head_type" type="QString"/>
                <Option value="1" name="is_curved" type="QString"/>
                <Option value="1" name="is_repeated" type="QString"/>
                <Option value="0" name="offset" type="QString"/>
                <Option value="MM" name="offset_unit" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="offset_unit_scale" type="QString"/>
                <Option value="0" name="ring_filter" type="QString"/>
              </Option>
              <prop v="4" k="arrow_start_width"/>
              <prop v="MM" k="arrow_start_width_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
              <prop v="0" k="arrow_type"/>
              <prop v="1.8" k="arrow_width"/>
              <prop v="MM" k="arrow_width_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
              <prop v="3.9" k="head_length"/>
              <prop v="MM" k="head_length_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
              <prop v="2.9" k="head_thickness"/>
              <prop v="MM" k="head_thickness_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
              <prop v="0" k="head_type"/>
              <prop v="1" k="is_curved"/>
              <prop v="1" k="is_repeated"/>
              <prop v="0" k="offset"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
              <prop v="0" k="ring_filter"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
              <symbol clip_to_extent="1" name="@@0@0@0" type="fill" alpha="1" force_rhr="0">
                <data_defined_properties>
                  <Option type="Map">
                    <Option value="" name="name" type="QString"/>
                    <Option name="properties"/>
                    <Option value="collection" name="type" type="QString"/>
                  </Option>
                </data_defined_properties>
                <layer pass="0" class="SimpleFill" enabled="1" locked="0">
                  <Option type="Map">
                    <Option value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale" type="QString"/>
                    <Option value="0,0,0,255" name="color" type="QString"/>
                    <Option value="bevel" name="joinstyle" type="QString"/>
                    <Option value="0,0" name="offset" type="QString"/>
                    <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
                    <Option value="MM" name="offset_unit" type="QString"/>
                    <Option value="255,255,255,255" name="outline_color" type="QString"/>
                    <Option value="solid" name="outline_style" type="QString"/>
                    <Option value="0.26" name="outline_width" type="QString"/>
                    <Option value="MM" name="outline_width_unit" type="QString"/>
                    <Option value="solid" name="style" type="QString"/>
                  </Option>
                  <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
                  <prop v="0,0,0,255" k="color"/>
                  <prop v="bevel" k="joinstyle"/>
                  <prop v="0,0" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MM" k="offset_unit"/>
                  <prop v="255,255,255,255" k="outline_color"/>
                  <prop v="solid" k="outline_style"/>
                  <prop v="0.26" k="outline_width"/>
                  <prop v="MM" k="outline_width_unit"/>
                  <prop v="solid" k="style"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option value="" name="name" type="QString"/>
                      <Option name="properties"/>
                      <Option value="collection" name="type" type="QString"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerGeometryType>1</layerGeometryType>
</qgis>
