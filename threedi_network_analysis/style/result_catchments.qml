<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingTol="1" version="3.10.10-A Coruña" labelsEnabled="0" simplifyLocal="1" readOnly="0" simplifyDrawingHints="1" simplifyMaxScale="1" minScale="1e+08" simplifyAlgorithm="0" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" type="categorizedSymbol" attr="location" enableorderby="0" symbollevels="0">
    <categories>
      <category render="true" value="upstream" symbol="0" label="Upstream"/>
      <category render="true" value="downstream" symbol="1" label="Downstream"/>
    </categories>
    <symbols>
      <symbol alpha="1" clip_to_extent="1" name="0" force_rhr="0" type="fill">
        <layer locked="0" enabled="1" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="227,26,28,64" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="227,26,28,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.8" k="outline_width"/>
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
      <symbol alpha="1" clip_to_extent="1" name="1" force_rhr="0" type="fill">
        <layer locked="0" enabled="1" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="11,178,181,64" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="11,178,181,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.8" k="outline_width"/>
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
    </symbols>
    <source-symbol>
      <symbol alpha="1" clip_to_extent="1" name="0" force_rhr="0" type="fill">
        <layer locked="0" enabled="1" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="232,25,18,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.8" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineWidth" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="1" name="type" type="int"/>
                  <Option value="" name="val" type="QString"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </source-symbol>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory lineSizeScale="3x:0,0,0,0,0,0" sizeScale="3x:0,0,0,0,0,0" diagramOrientation="Up" minimumSize="0" backgroundColor="#ffffff" scaleDependency="Area" labelPlacementMethod="XHeight" enabled="0" backgroundAlpha="255" scaleBasedVisibility="0" sizeType="MM" penWidth="0" width="15" penColor="#000000" penAlpha="255" lineSizeType="MM" opacity="1" barWidth="5" height="15" minScaleDenominator="0" rotationOffset="270" maxScaleDenominator="1e+08">
      <fontProperties style="" description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0"/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="1" priority="0" showAll="1" obstacle="0" linePlacementFlags="18" dist="0" zIndex="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option name="QgsGeometryGapCheck" type="Map">
        <Option value="0" name="allowedGapsBuffer" type="double"/>
        <Option value="false" name="allowedGapsEnabled" type="bool"/>
        <Option value="" name="allowedGapsLayer" type="QString"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <fieldConfiguration>
    <field name="id">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="node_type">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="node_type_description">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="location">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="catchment_id">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="from_polygon">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="id" index="0" name=""/>
    <alias field="node_type" index="1" name=""/>
    <alias field="node_type_description" index="2" name=""/>
    <alias field="location" index="3" name=""/>
    <alias field="catchment_id" index="4" name=""/>
    <alias field="from_polygon" index="5" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="id" expression="" applyOnUpdate="0"/>
    <default field="node_type" expression="" applyOnUpdate="0"/>
    <default field="node_type_description" expression="" applyOnUpdate="0"/>
    <default field="location" expression="" applyOnUpdate="0"/>
    <default field="catchment_id" expression="" applyOnUpdate="0"/>
    <default field="from_polygon" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="id" constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="node_type" constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="node_type_description" constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="location" constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="catchment_id" constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="from_polygon" constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" exp="" desc=""/>
    <constraint field="node_type" exp="" desc=""/>
    <constraint field="node_type_description" exp="" desc=""/>
    <constraint field="location" exp="" desc=""/>
    <constraint field="catchment_id" exp="" desc=""/>
    <constraint field="from_polygon" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column hidden="1" width="-1" type="actions"/>
      <column hidden="0" width="-1" name="id" type="field"/>
      <column hidden="0" width="-1" name="catchment_id" type="field"/>
      <column hidden="0" width="-1" name="from_polygon" type="field"/>
      <column hidden="0" width="-1" name="location" type="field"/>
      <column hidden="0" width="-1" name="node_type" type="field"/>
      <column hidden="0" width="-1" name="node_type_description" type="field"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="catchment_id" editable="1"/>
    <field name="from_polygon" editable="1"/>
    <field name="id" editable="1"/>
    <field name="location" editable="1"/>
    <field name="node_type" editable="1"/>
    <field name="node_type_description" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="catchment_id" labelOnTop="0"/>
    <field name="from_polygon" labelOnTop="0"/>
    <field name="id" labelOnTop="0"/>
    <field name="location" labelOnTop="0"/>
    <field name="node_type" labelOnTop="0"/>
    <field name="node_type_description" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>"id"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
