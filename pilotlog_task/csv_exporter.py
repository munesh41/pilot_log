import pandas as pd

from .models import Aircraft, Flight


def export_to_csv(file_path):
    # Export Aircraft data
    aircraft_fields = [
        "id",
        "equipment_type",
        "type_code",
        "year",
        "make",
        "model",
        "category",
        "aircraft_class",
        "gear_type",
        "engine_type",
        "complex",
        "high_performance",
        "pressurized",
        "taa",
    ]
    aircraft_queryset = Aircraft.objects.values(*aircraft_fields)
    aircraft_df = pd.DataFrame.from_records(aircraft_queryset)
    aircraft_df.rename(
        columns={
            "id": "AircraftID",
            "equipment_type": "EquipmentType",
            "type_code": "TypeCode",
            "year": "Year",
            "make": "Make",
            "model": "Model",
            "category": "Category",
            "aircraft_class": "Class",
            "gear_type": "GearType",
            "engine_type": "EngineType",
            "complex": "Complex",
            "high_performance": "HighPerformance",
            "pressurized": "Pressurized",
            "taa": "TAA",
        },
        inplace=True,
    )

    # Export Flight data
    flight_fields = [
        "date_utc",
        "aircraft__id",
        "from_airport",
        "to_airport",
        "route",
        "time_out",
        "time_off",
        "time_on",
        "time_in",
        "on_duty",
        "off_duty",
        "total_time",
        "pic",
        "sic",
        "night",
        "solo",
        "cross_country",
        "nvg",
        "nvg_ops",
        "distance",
        "day_takeoffs",
        "day_landings_full_stop",
        "night_takeoffs",
        "night_landings_full_stop",
        "all_landings",
        "actual_instrument",
        "simulated_instrument",
        "hobbs_start",
        "hobbs_end",
        "tach_start",
        "tach_end",
        "holds",
        "approach1",
        "approach2",
        "approach3",
        "approach4",
        "approach5",
        "approach6",
        "dual_given",
        "dual_received",
        "simulated_flight",
        "ground_training",
        "instructor_name",
        "instructor_comments",
        "person1",
        "person2",
        "person3",
        "person4",
        "person5",
        "person6",
        "flight_review",
        "checkride",
        "ipc",
        "nvg_proficiency",
        "faa6158",
        "custom_text",
        "custom_numeric",
        "custom_hours",
        "custom_counter",
        "custom_date",
        "custom_datetime",
        "custom_toggle",
        "pilot_comments",
    ]
    flight_queryset = Flight.objects.values(*flight_fields)
    flight_df = pd.DataFrame.from_records(flight_queryset)
    flight_df.rename(
        columns={
            "date_utc": "Date",
            "aircraft__id": "AircraftID",
            "from_airport": "From",
            "to_airport": "To",
            "route": "Route",
            "time_out": "TimeOut",
            "time_off": "TimeOff",
            "time_on": "TimeOn",
            "time_in": "TimeIn",
            "on_duty": "OnDuty",
            "off_duty": "OffDuty",
            "total_time": "TotalTime",
            "pic": "PIC",
            "sic": "SIC",
            "night": "Night",
            "solo": "Solo",
            "cross_country": "CrossCountry",
            "nvg": "NVG",
            "nvg_ops": "NVGOps",
            "distance": "Distance",
            "day_takeoffs": "DayTakeoffs",
            "day_landings_full_stop": "DayLandingsFullStop",
            "night_takeoffs": "NightTakeoffs",
            "night_landings_full_stop": "NightLandingsFullStop",
            "all_landings": "AllLandings",
            "actual_instrument": "ActualInstrument",
            "simulated_instrument": "SimulatedInstrument",
            "hobbs_start": "HobbsStart",
            "hobbs_end": "HobbsEnd",
            "tach_start": "TachStart",
            "tach_end": "TachEnd",
            "holds": "Holds",
            "approach1": "Approach1",
            "approach2": "Approach2",
            "approach3": "Approach3",
            "approach4": "Approach4",
            "approach5": "Approach5",
            "approach6": "Approach6",
            "dual_given": "DualGiven",
            "dual_received": "DualReceived",
            "simulated_flight": "SimulatedFlight",
            "ground_training": "GroundTraining",
            "instructor_name": "InstructorName",
            "instructor_comments": "InstructorComments",
            "person1": "Person1",
            "person2": "Person2",
            "person3": "Person3",
            "person4": "Person4",
            "person5": "Person5",
            "person6": "Person6",
            "flight_review": "FlightReview",
            "checkride": "Checkride",
            "ipc": "IPC",
            "nvg_proficiency": "NVGProficiency",
            "faa6158": "FAA6158",
            "custom_text": "CustomFieldName",
            "custom_numeric": "CustomFieldName",
            "custom_hours": "CustomFieldName",
            "custom_counter": "CustomFieldName",
            "custom_date": "CustomFieldName",
            "custom_datetime": "CustomFieldName",
            "custom_toggle": "CustomFieldName",
            "pilot_comments": "PilotComments",
        },
        inplace=True,
    )

    # Create a combined CSV
    with open(file_path, "w", newline="") as csvfile:
        # Write Aircraft Table
        csvfile.write(
            "Aircraft Table,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n"
        )
        aircraft_df.to_csv(csvfile, index=False, mode="a")
        csvfile.write(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n")
        csvfile.write(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n")

        # Write Flights Table
        csvfile.write(
            "Flights Table,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,#;type;runway;airport;comments,,,,,,,,,,,,name;role;email,,,,,,,,,,,,,,,,,,,\n"
        )
        flight_df.to_csv(csvfile, index=False, mode="a")
