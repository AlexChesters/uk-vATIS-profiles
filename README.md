# uk-vATIS-profiles
vATIS profiles for UK VATSIM controllers

# Downloads
You can download the profiles [here](https://projects.alexchesters.com/uk-vATIS-profiles/main/uk-vatis-profiles.zip).

# Development
Profiles are defined as `yaml` files, which are then built into the JSON files used by vATIS. The
[`profiles/`](./profiles/) directory contains all profiles in the following structure:
```
profiles/
  <POSITION>/
    <AIRFIELD>.yml
```

For example, a profile for Manchester Ground would be in the following structure:
```
profiles/
  gmc/
    egcc.yml
```

Below is an example profile for a Manchester Ground controller:
```yaml
name: Manchester
code: EGCC
atis_frequency: 21855
presets:
  - name: RUNWAY 23R (single-runway operations)
    runway_identifier: "23R"
    conditions: SINGLE RUNWAY OPERATIONS
  - name: RUNWAY 05L (single-runway operations)
    runway_identifier: "05L"
    conditions: SINGLE RUNWAY OPERATIONS
transition_levels:
  - low: 940
    high: 958
    altitude: 80
  - low: 959
    high: 976
    altitude: 75
  - low: 977
    high: 994
    altitude: 70
  - low: 995
    high: 1012
    altitude: 65
  - low: 1013
    high: 1031
    altitude: 60
  - low: 1032
    high: 1049
    altitude: 55
  - low: 1050
    high: 1060
    altitude: 50
closing_statement: DEPARTING AIRCRAFT REPORT STAND NUMBER AND AIRCRAFT TYPE TO MANCHESTER GROUND ON 121.855
```

# Acknowledgements
Thanks to [Lenny](https://github.com/lennycolton/vATIS-Profiles), [RedstonePilot](https://github.com/RedstonePilot/vATIS-Profiles) and
[Fraser](https://community.vatsim.uk/topic/38856-unofficial-guide-vatis-generic-setup-and-configuration/#comment-350271) whose profiles have been a very useful starting point for these.
