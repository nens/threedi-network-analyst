<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="100000000" simplifyDrawingTol="1" simplifyMaxScale="1" simplifyLocal="1" version="3.14.16-Pi" maxScale="0" styleCategories="AllStyleCategories" simplifyDrawingHints="1" hasScaleBasedVisibilityFlag="0" simplifyAlgorithm="0" labelsEnabled="0" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>0</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal startField="" enabled="0" startExpression="" durationField="" durationUnit="min" fixedDuration="0" accumulate="0" mode="0" endField="" endExpression="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 symbollevels="0" forceraster="0" enableorderby="0" type="categorizedSymbol" attr="location">
    <categories>
      <category value="upstream" symbol="0" render="true" label="Upstream"/>
      <category value="downstream" symbol="1" render="true" label="Downstream"/>
    </categories>
    <symbols>
      <symbol name="0" alpha="1" clip_to_extent="1" type="fill" force_rhr="0">
        <layer locked="0" pass="0" enabled="1" class="SimpleFill">
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
      <symbol name="1" alpha="1" clip_to_extent="1" type="fill" force_rhr="0">
        <layer locked="0" pass="0" enabled="1" class="SimpleFill">
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
      <symbol name="0" alpha="1" clip_to_extent="1" type="fill" force_rhr="0">
        <layer locked="0" pass="0" enabled="1" class="SimpleLine">
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
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory spacingUnit="MM" backgroundAlpha="255" barWidth="5" lineSizeType="MM" rotationOffset="270" lineSizeScale="3x:0,0,0,0,0,0" height="15" sizeScale="3x:0,0,0,0,0,0" penWidth="0" penColor="#000000" direction="0" backgroundColor="#ffffff" opacity="1" scaleDependency="Area" showAxis="1" maxScaleDenominator="1e+08" spacing="5" diagramOrientation="Up" enabled="0" spacingUnitScale="3x:0,0,0,0,0,0" penAlpha="255" minScaleDenominator="0" sizeType="MM" labelPlacementMethod="XHeight" scaleBasedVisibility="0" width="15" minimumSize="0">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
      <axisSymbol>
        <symbol name="" alpha="1" clip_to_extent="1" type="line" force_rhr="0">
          <layer locked="0" pass="0" enabled="1" class="SimpleLine">
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
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
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" priority="0" zIndex="0" dist="0" placement="1" showAll="1" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option name="QgsGeometryGapCheck" type="Map">
        <Option value="0" name="allowedGapsBuffer" type="double"/>
        <Option value="false" name="allowedGapsEnabled" type="bool"/>
        <Option value="" name="allowedGapsLayer" type="QString"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <referencedLayers/>
  <referencingLayers/>
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
    <default expression="" field="id" applyOnUpdate="0"/>
    <default expression="" field="node_type" applyOnUpdate="0"/>
    <default expression="" field="node_type_description" applyOnUpdate="0"/>
    <default expression="" field="location" applyOnUpdate="0"/>
    <default expression="" field="catchment_id" applyOnUpdate="0"/>
    <default expression="" field="from_polygon" applyOnUpdate="0"/>
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
    <constraint desc="" field="id" exp=""/>
    <constraint desc="" field="node_type" exp=""/>
    <constraint desc="" field="node_type_description" exp=""/>
    <constraint desc="" field="location" exp=""/>
    <constraint desc="" field="catchment_id" exp=""/>
    <constraint desc="" field="from_polygon" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="actions" width="-1" hidden="1"/>
      <column name="id" type="field" width="-1" hidden="0"/>
      <column name="catchment_id" type="field" width="-1" hidden="0"/>
      <column name="from_polygon" type="field" width="-1" hidden="0"/>
      <column name="location" type="field" width="-1" hidden="0"/>
      <column name="node_type" type="field" width="-1" hidden="0"/>
      <column name="node_type_description" type="field" width="-1" hidden="0"/>
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
    <field editable="1" name="catchment_id"/>
    <field editable="1" name="from_polygon"/>
    <field editable="1" name="id"/>
    <field editable="1" name="location"/>
    <field editable="1" name="node_type"/>
    <field editable="1" name="node_type_description"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="catchment_id"/>
    <field labelOnTop="0" name="from_polygon"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="location"/>
    <field labelOnTop="0" name="node_type"/>
    <field labelOnTop="0" name="node_type_description"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"id"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
