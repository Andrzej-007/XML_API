

<?xml version="1.0" encoding="UTF-8" ?>
<menu>
  <column>
    <header>File</header>
    <items>
       <id>Open</id>
       <label>Open</label>
    </items>
    <items>
       <id>New</id>
       <label>New</label>
    </items>
    ...
  </column>
  ...
</menu>

<!-- Everything in between is ignored This element should be removed -->




{
    "menu": [
            { "header": "File",
               "items": [
                        {"id": "Open", "label": "Open"},
                        {"id": "New", "label": "New"},
                        {"id": "Close", "label": "Close"}
                        ]
            },
            { "header": "View",
              "items": [
                        {"id": "ZoomIn", "label": "Zoom In"},
                        {"id": "ZoomOut", "label": "Zoom Out"},
                        {"id": "OriginalView", "label": "Original View"}
                        ]
            }
            ]
}

print('**********************************************')
"""below xml example """

<? xml version = "1.0" >

<Monday_forcast>
    <description>sunny</description>
    <date>2015-06-01</date>
    <maxTemp unit="C">22</maxTemp>
    <minTemp unit="C">19</minTemp>
    <windSpeed unit="kph">0</windSpeed>
    <danger>False</danger>
</Monday_forcast>


print('**********************************************')
""" below JSON example """
temperature_data = {
                    "Monday":
                            {"description":"sunny",
                             "maxTemp":22,
                             "minTemp":20,
                             "windSpeed":12,
                             "danger":'false'
                            }
                    }
print('**********************************************')
# print(temperature_data)
print(" ")

<?xml version="1.0" ?>
<Forcast>
    <Monday_forcast>
        <description>sunny</description>
        <date>2015-06-01</date>
        <maxTemp unit="C">22</maxTemp>
        <minTemp unit="C">19</minTemp>
        <windSpeed unit="kph">3</windSpeed>
        <danger>False</danger>
    </Monday_forcast>
    <Tuesday_forcast>
        <description>winndy</description>
        <date>2015-06-02</date>
        <maxTemp unit="C">22</maxTemp>
        <minTemp unit="C">19</minTemp>
        <windSpeed unit="kph">40</windSpeed>
        <danger>True</danger>
    </Tuesday_forcast>
    <Wednesday_forcast/>  <!-- "We don't have forecast for Wednesday yet" -->
</Forcast>


print('**********************************************')

three_date_forcast ={
                    "Forcast": [{"Monday": {"description":"sunny",
                                            "maxTemp":22,
                                            "minTemp":20,
                                            "windSpeed":12,
                                            "danger":'false'
                                            }
                                },
                                {"Tuesday": {"description":"stormy",
                                             "maxTemp":22,
                                             "minTemp":20,
                                             "windSpeed":12,
                                             "danger":'false'
                                            }
                                },
                                {"Wednesday":{"description":"raining",
                                             "maxTemp":22,
                                             "minTemp":20,
                                             "windSpeed":12,
                                             "danger":'false'
                                            }
                                }
                                ]
                    }
print(three_date_forcast)
