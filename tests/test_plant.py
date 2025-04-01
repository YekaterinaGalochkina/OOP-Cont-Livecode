from classes.plant import Plant

def test_plant_class_instantiation():
    # arrange
    name = "Orchid"
    water_level = 5
    sunlight_hours = 3
    is_blooming = True

    # act
    plant = Plant(name, water_level, sunlight_hours, is_blooming)

    # assert
    assert plant.name == name
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming == is_blooming


def test_plant_class_instantiation_default_is_blooming():
    # arrange
    name = "Orchid"
    water_level = 5
    sunlight_hours = 3

    # act
    plant = Plant(name, water_level, sunlight_hours)

    # assert
    assert plant.name == name
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming == False


def test_change_water_increases_water_level():
    # arrange
    name = "Oxalis"
    water_level = 2
    sunlight_hours = 7
    is_blooming = True
    amount_to_add = 3

    plant = Plant(name, water_level, sunlight_hours, is_blooming)

    #act
    new_water_level = plant.change_water(amount_to_add)

    # assert
    assert plant.water_level == 5
    assert new_water_level == 5


def test_check_growth_water_sunlight_over_five():
    # arrange
    name = "Purple Trumpet"
    water_level = 6
    sunlight_hours = 6
    is_blooming = False

    plant = Plant(name, water_level, sunlight_hours, is_blooming)

    # act
    result = plant.check_growth()

    # assert
    assert result == "Purple Trumpet's growth stage: Mature"
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert not plant.is_blooming

