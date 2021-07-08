recipe = {
    "speed-module": {
        "name": "speed-module",
        "energy_required": 15.0,
        "ingredients": {
            "advanced-circuit": 5,
            "electronic-circuit": 5
        },
        "results": {
            "speed-module": 1
        },
        "icon": "__base__/graphics/icons/speed-module.png",
        "subgroup": "module"
    },
    "speed-module-2": {
        "name": "speed-module-2",
        "energy_required": 30.0,
        "ingredients": {
            "speed-module": 4,
            "advanced-circuit": 5,
            "processing-unit": 5
        },
        "results": {
            "speed-module-2": 1
        },
        "icon": "__base__/graphics/icons/speed-module-2.png",
        "subgroup": "module"
    },
    "speed-module-3": {
        "name": "speed-module-3",
        "energy_required": 60.0,
        "ingredients": {
            "speed-module-2": 5,
            "advanced-circuit": 5,
            "processing-unit": 5
        },
        "results": {
            "speed-module-3": 1
        },
        "icon": "__base__/graphics/icons/speed-module-3.png",
        "subgroup": "module"
    },
    "productivity-module": {
        "name": "productivity-module",
        "energy_required": 15.0,
        "ingredients": {
            "advanced-circuit": 5,
            "electronic-circuit": 5
        },
        "results": {
            "productivity-module": 1
        },
        "icon": "__base__/graphics/icons/productivity-module.png",
        "subgroup": "module"
    },
    "productivity-module-2": {
        "name": "productivity-module-2",
        "energy_required": 30.0,
        "ingredients": {
            "productivity-module": 4,
            "advanced-circuit": 5,
            "processing-unit": 5
        },
        "results": {
            "productivity-module-2": 1
        },
        "icon": "__base__/graphics/icons/productivity-module-2.png",
        "subgroup": "module"
    },
    "productivity-module-3": {
        "name": "productivity-module-3",
        "energy_required": 60.0,
        "ingredients": {
            "productivity-module-2": 5,
            "advanced-circuit": 5,
            "processing-unit": 5
        },
        "results": {
            "productivity-module-3": 1
        },
        "icon": "__base__/graphics/icons/productivity-module-3.png",
        "subgroup": "module"
    },
    "effectivity-module": {
        "name": "effectivity-module",
        "energy_required": 15.0,
        "ingredients": {
            "advanced-circuit": 5,
            "electronic-circuit": 5
        },
        "results": {
            "effectivity-module": 1
        },
        "icon": "__base__/graphics/icons/effectivity-module.png",
        "subgroup": "module"
    },
    "effectivity-module-2": {
        "name": "effectivity-module-2",
        "energy_required": 30.0,
        "ingredients": {
            "effectivity-module": 4,
            "advanced-circuit": 5,
            "processing-unit": 5
        },
        "results": {
            "effectivity-module-2": 1
        },
        "icon": "__base__/graphics/icons/effectivity-module-2.png",
        "subgroup": "module"
    },
    "effectivity-module-3": {
        "name": "effectivity-module-3",
        "energy_required": 60.0,
        "ingredients": {
            "effectivity-module-2": 5,
            "advanced-circuit": 5,
            "processing-unit": 5
        },
        "results": {
            "effectivity-module-3": 1
        },
        "icon": "__base__/graphics/icons/effectivity-module-3.png",
        "subgroup": "module"
    },
    "stack-inserter": {
        "name": "stack-inserter",
        "energy_required": 0.5,
        "ingredients": {
            "iron-gear-wheel": 15,
            "electronic-circuit": 15,
            "advanced-circuit": 1,
            "fast-inserter": 1
        },
        "results": {
            "stack-inserter": 1
        },
        "icon": "__base__/graphics/icons/stack-inserter.png",
        "subgroup": "inserter"
    },
    "stack-filter-inserter": {
        "name": "stack-filter-inserter",
        "energy_required": 0.5,
        "ingredients": {
            "stack-inserter": 1,
            "electronic-circuit": 5
        },
        "results": {
            "stack-filter-inserter": 1
        },
        "icon": "__base__/graphics/icons/stack-filter-inserter.png",
        "subgroup": "inserter"
    },
    "basic-oil-processing": {
        "name": "basic-oil-processing",
        "energy_required": 5.0,
        "ingredients": {
            "crude-oil": 100
        },
        "results": {
            "petroleum-gas": 45
        }
    },
    "advanced-oil-processing": {
        "name": "advanced-oil-processing",
        "energy_required": 5.0,
        "ingredients": {
            "water": 50,
            "crude-oil": 100
        },
        "results": {
            "heavy-oil": 25,
            "light-oil": 45,
            "petroleum-gas": 55
        }
    },
    "coal-liquefaction": {
        "name": "coal-liquefaction",
        "energy_required": 5.0,
        "ingredients": {
            "coal": 10,
            "heavy-oil": 25,
            "steam": 50
        },
        "results": {
            "heavy-oil": 90,
            "light-oil": 20,
            "petroleum-gas": 10
        }
    },
    "heavy-oil-cracking": {
        "name": "heavy-oil-cracking",
        "energy_required": 2.0,
        "ingredients": {
            "water": 30,
            "heavy-oil": 40
        },
        "results": {
            "light-oil": 30
        }
    },
    "light-oil-cracking": {
        "name": "light-oil-cracking",
        "energy_required": 2.0,
        "ingredients": {
            "water": 30,
            "light-oil": 30
        },
        "results": {
            "petroleum-gas": 20
        }
    },
    "sulfuric-acid": {
        "name": "sulfuric-acid",
        "energy_required": 1.0,
        "ingredients": {
            "sulfur": 5,
            "iron-plate": 1,
            "water": 100
        },
        "results": {
            "sulfuric-acid": 50
        }
    },
    "plastic-bar": {
        "name": "plastic-bar",
        "energy_required": 1.0,
        "ingredients": {
            "petroleum-gas": 20,
            "coal": 1
        },
        "results": {
            "plastic-bar": 2
        },
        "icon": "__base__/graphics/icons/plastic-bar.png",
        "subgroup": "raw-material"
    },
    "solid-fuel-from-light-oil": {
        "name": "solid-fuel-from-light-oil",
        "energy_required": 2.0,
        "ingredients": {
            "light-oil": 10
        },
        "results": {
            "solid-fuel": 1
        }
    },
    "solid-fuel-from-petroleum-gas": {
        "name": "solid-fuel-from-petroleum-gas",
        "energy_required": 2.0,
        "ingredients": {
            "petroleum-gas": 20
        },
        "results": {
            "solid-fuel": 1
        }
    },
    "solid-fuel-from-heavy-oil": {
        "name": "solid-fuel-from-heavy-oil",
        "energy_required": 2.0,
        "ingredients": {
            "heavy-oil": 20
        },
        "results": {
            "solid-fuel": 1
        }
    },
    "sulfur": {
        "name": "sulfur",
        "energy_required": 1.0,
        "ingredients": {
            "water": 30,
            "petroleum-gas": 30
        },
        "results": {
            "sulfur": 2
        },
        "icon": "__base__/graphics/icons/sulfur.png",
        "subgroup": "raw-material"
    },
    "lubricant": {
        "name": "lubricant",
        "energy_required": 1.0,
        "ingredients": {
            "heavy-oil": 10
        },
        "results": {
            "lubricant": 10
        }
    },
    "empty-barrel": {
        "name": "empty-barrel",
        "energy_required": 1.0,
        "ingredients": {
            "steel-plate": 1
        },
        "results": {
            "empty-barrel": 1
        },
        "icon": "__base__/graphics/icons/fluid/barreling/empty-barrel.png",
        "subgroup": "intermediate-product"
    },
    "night-vision-equipment": {
        "name": "night-vision-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "advanced-circuit": 5,
            "steel-plate": 10
        },
        "results": {
            "night-vision-equipment": 1
        },
        "icon": "__base__/graphics/icons/night-vision-equipment.png",
        "subgroup": "equipment"
    },
    "belt-immunity-equipment": {
        "name": "belt-immunity-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "advanced-circuit": 5,
            "steel-plate": 10
        },
        "results": {
            "belt-immunity-equipment": 1
        },
        "icon": "__base__/graphics/icons/belt-immunity-equipment.png",
        "subgroup": "equipment"
    },
    "energy-shield-equipment": {
        "name": "energy-shield-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "advanced-circuit": 5,
            "steel-plate": 10
        },
        "results": {
            "energy-shield-equipment": 1
        },
        "icon": "__base__/graphics/icons/energy-shield-equipment.png",
        "subgroup": "military-equipment"
    },
    "energy-shield-mk2-equipment": {
        "name": "energy-shield-mk2-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "energy-shield-equipment": 10,
            "processing-unit": 5,
            "low-density-structure": 5
        },
        "results": {
            "energy-shield-mk2-equipment": 1
        },
        "icon": "__base__/graphics/icons/energy-shield-mk2-equipment.png",
        "subgroup": "military-equipment"
    },
    "battery-equipment": {
        "name": "battery-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "battery": 5,
            "steel-plate": 10
        },
        "results": {
            "battery-equipment": 1
        },
        "icon": "__base__/graphics/icons/battery-equipment.png",
        "subgroup": "equipment"
    },
    "battery-mk2-equipment": {
        "name": "battery-mk2-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "battery-equipment": 10,
            "processing-unit": 15,
            "low-density-structure": 5
        },
        "results": {
            "battery-mk2-equipment": 1
        },
        "icon": "__base__/graphics/icons/battery-mk2-equipment.png",
        "subgroup": "equipment"
    },
    "solar-panel-equipment": {
        "name": "solar-panel-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "solar-panel": 1,
            "advanced-circuit": 2,
            "steel-plate": 5
        },
        "results": {
            "solar-panel-equipment": 1
        }
    },
    "fusion-reactor-equipment": {
        "name": "fusion-reactor-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "processing-unit": 200,
            "low-density-structure": 50
        },
        "results": {
            "fusion-reactor-equipment": 1
        },
        "icon": "__base__/graphics/icons/fusion-reactor-equipment.png",
        "subgroup": "equipment"
    },
    "personal-laser-defense-equipment": {
        "name": "personal-laser-defense-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "processing-unit": 20,
            "low-density-structure": 5,
            "laser-turret": 5
        },
        "results": {
            "personal-laser-defense-equipment": 1
        },
        "icon": "__base__/graphics/icons/personal-laser-defense-equipment.png",
        "subgroup": "military-equipment"
    },
    "discharge-defense-equipment": {
        "name": "discharge-defense-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "processing-unit": 5,
            "steel-plate": 20,
            "laser-turret": 10
        },
        "results": {
            "discharge-defense-equipment": 1
        },
        "icon": "__base__/graphics/icons/discharge-defense-equipment.png",
        "subgroup": "military-equipment"
    },
    "discharge-defense-remote": {
        "name": "discharge-defense-remote",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 1
        },
        "results": {
            "discharge-defense-remote": 1
        },
        "icon": "__base__/graphics/icons/discharge-defense-equipment-controller.png",
        "subgroup": "military-equipment"
    },
    "exoskeleton-equipment": {
        "name": "exoskeleton-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "processing-unit": 10,
            "electric-engine-unit": 30,
            "steel-plate": 20
        },
        "results": {
            "exoskeleton-equipment": 1
        },
        "icon": "__base__/graphics/icons/exoskeleton-equipment.png",
        "subgroup": "equipment"
    },
    "personal-roboport-equipment": {
        "name": "personal-roboport-equipment",
        "energy_required": 10.0,
        "ingredients": {
            "advanced-circuit": 10,
            "iron-gear-wheel": 40,
            "steel-plate": 20,
            "battery": 45
        },
        "results": {
            "personal-roboport-equipment": 1
        },
        "icon": "__base__/graphics/icons/personal-roboport-equipment.png",
        "subgroup": "equipment"
    },
    "personal-roboport-mk2-equipment": {
        "name": "personal-roboport-mk2-equipment",
        "energy_required": 20.0,
        "ingredients": {
            "personal-roboport-equipment": 5,
            "processing-unit": 100,
            "low-density-structure": 20
        },
        "results": {
            "personal-roboport-mk2-equipment": 1
        },
        "icon": "__base__/graphics/icons/personal-roboport-mk2-equipment.png",
        "subgroup": "equipment"
    },
    "laser-turret": {
        "name": "laser-turret",
        "energy_required": 20.0,
        "ingredients": {
            "steel-plate": 20,
            "electronic-circuit": 20,
            "battery": 12
        },
        "results": {
            "laser-turret": 1
        },
        "icon": "__base__/graphics/icons/laser-turret.png",
        "subgroup": "defensive-structure"
    },
    "flamethrower-turret": {
        "name": "flamethrower-turret",
        "energy_required": 20.0,
        "ingredients": {
            "steel-plate": 30,
            "iron-gear-wheel": 15,
            "pipe": 10,
            "engine-unit": 5
        },
        "results": {
            "flamethrower-turret": 1
        },
        "icon": "__base__/graphics/icons/flamethrower-turret.png",
        "subgroup": "defensive-structure"
    },
    "artillery-turret": {
        "name": "artillery-turret",
        "energy_required": 40.0,
        "ingredients": {
            "steel-plate": 60,
            "concrete": 60,
            "iron-gear-wheel": 40,
            "advanced-circuit": 20
        },
        "results": {
            "artillery-turret": 1
        },
        "icon": "__base__/graphics/icons/artillery-turret.png",
        "subgroup": "defensive-structure"
    },
    "artillery-targeting-remote": {
        "name": "artillery-targeting-remote",
        "energy_required": 0.5,
        "ingredients": {
            "processing-unit": 1,
            "radar": 1
        },
        "results": {
            "artillery-targeting-remote": 1
        },
        "icon": "__base__/graphics/icons/artillery-targeting-remote.png",
        "subgroup": "defensive-structure"
    },
    "gun-turret": {
        "name": "gun-turret",
        "energy_required": 8.0,
        "ingredients": {
            "iron-gear-wheel": 10,
            "copper-plate": 10,
            "iron-plate": 20
        },
        "results": {
            "gun-turret": 1
        },
        "icon": "__base__/graphics/icons/gun-turret.png",
        "subgroup": "defensive-structure"
    },
    "wooden-chest": {
        "name": "wooden-chest",
        "energy_required": 0.5,
        "ingredients": {
            "wood": 2
        },
        "results": {
            "wooden-chest": 1
        },
        "icon": "__base__/graphics/icons/wooden-chest.png",
        "subgroup": "storage"
    },
    "iron-stick": {
        "name": "iron-stick",
        "energy_required": 0.5,
        "ingredients": {
            "iron-plate": 1
        },
        "results": {
            "iron-stick": 2
        },
        "icon": "__base__/graphics/icons/iron-stick.png",
        "subgroup": "intermediate-product"
    },
    "stone-furnace": {
        "name": "stone-furnace",
        "energy_required": 0.5,
        "ingredients": {
            "stone": 5
        },
        "results": {
            "stone-furnace": 1
        },
        "icon": "__base__/graphics/icons/stone-furnace.png",
        "subgroup": "smelting-machine"
    },
    "boiler": {
        "name": "boiler",
        "energy_required": 0.5,
        "ingredients": {
            "stone-furnace": 1,
            "pipe": 4
        },
        "results": {
            "boiler": 1
        },
        "icon": "__base__/graphics/icons/boiler.png",
        "subgroup": "energy"
    },
    "steam-engine": {
        "name": "steam-engine",
        "energy_required": 0.5,
        "ingredients": {
            "iron-gear-wheel": 8,
            "pipe": 5,
            "iron-plate": 10
        },
        "results": {
            "steam-engine": 1
        },
        "icon": "__base__/graphics/icons/steam-engine.png",
        "subgroup": "energy"
    },
    "iron-gear-wheel": {
        "name": "iron-gear-wheel",
        "energy_required": 0.5,
        "ingredients": {
            "iron-plate": 2
        },
        "results": {
            "iron-gear-wheel": 1
        },
        "icon": "__base__/graphics/icons/iron-gear-wheel.png",
        "subgroup": "intermediate-product"
    },
    "electronic-circuit": {
        "name": "electronic-circuit",
        "energy_required": 0.5,
        "ingredients": {
            "iron-plate": 1,
            "copper-cable": 3
        },
        "results": {
            "electronic-circuit": 1
        },
        "icon": "__base__/graphics/icons/electronic-circuit.png",
        "subgroup": "intermediate-product"
    },
    "transport-belt": {
        "name": "transport-belt",
        "energy_required": 0.5,
        "ingredients": {
            "iron-plate": 1,
            "iron-gear-wheel": 1
        },
        "results": {
            "transport-belt": 2
        },
        "icon": "__base__/graphics/icons/transport-belt.png",
        "subgroup": "belt"
    },
    "electric-mining-drill": {
        "name": "electric-mining-drill",
        "energy_required": 2.0,
        "ingredients": {
            "electronic-circuit": 3,
            "iron-gear-wheel": 5,
            "iron-plate": 10
        },
        "results": {
            "electric-mining-drill": 1
        },
        "icon": "__base__/graphics/icons/electric-mining-drill.png",
        "subgroup": "extraction-machine"
    },
    "burner-mining-drill": {
        "name": "burner-mining-drill",
        "energy_required": 2.0,
        "ingredients": {
            "iron-gear-wheel": 3,
            "stone-furnace": 1,
            "iron-plate": 3
        },
        "results": {
            "burner-mining-drill": 1
        },
        "icon": "__base__/graphics/icons/burner-mining-drill.png",
        "subgroup": "extraction-machine"
    },
    "inserter": {
        "name": "inserter",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 1,
            "iron-gear-wheel": 1,
            "iron-plate": 1
        },
        "results": {
            "inserter": 1
        },
        "icon": "__base__/graphics/icons/inserter.png",
        "subgroup": "inserter"
    },
    "fast-inserter": {
        "name": "fast-inserter",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 2,
            "iron-plate": 2,
            "inserter": 1
        },
        "results": {
            "fast-inserter": 1
        },
        "icon": "__base__/graphics/icons/fast-inserter.png",
        "subgroup": "inserter"
    },
    "filter-inserter": {
        "name": "filter-inserter",
        "energy_required": 0.5,
        "ingredients": {
            "fast-inserter": 1,
            "electronic-circuit": 4
        },
        "results": {
            "filter-inserter": 1
        },
        "icon": "__base__/graphics/icons/filter-inserter.png",
        "subgroup": "inserter"
    },
    "long-handed-inserter": {
        "name": "long-handed-inserter",
        "energy_required": 0.5,
        "ingredients": {
            "iron-gear-wheel": 1,
            "iron-plate": 1,
            "inserter": 1
        },
        "results": {
            "long-handed-inserter": 1
        },
        "icon": "__base__/graphics/icons/long-handed-inserter.png",
        "subgroup": "inserter"
    },
    "burner-inserter": {
        "name": "burner-inserter",
        "energy_required": 0.5,
        "ingredients": {
            "iron-plate": 1,
            "iron-gear-wheel": 1
        },
        "results": {
            "burner-inserter": 1
        },
        "icon": "__base__/graphics/icons/burner-inserter.png",
        "subgroup": "inserter"
    },
    "pipe": {
        "name": "pipe",
        "energy_required": 0.5,
        "ingredients": {
            "iron-plate": 1
        },
        "results": {
            "pipe": 1
        },
        "icon": "__base__/graphics/icons/pipe.png",
        "subgroup": "energy-pipe-distribution"
    },
    "offshore-pump": {
        "name": "offshore-pump",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 2,
            "pipe": 1,
            "iron-gear-wheel": 1
        },
        "results": {
            "offshore-pump": 1
        },
        "icon": "__base__/graphics/icons/offshore-pump.png",
        "subgroup": "extraction-machine"
    },
    "copper-cable": {
        "name": "copper-cable",
        "energy_required": 0.5,
        "ingredients": {
            "copper-plate": 1
        },
        "results": {
            "copper-cable": 2
        },
        "icon": "__base__/graphics/icons/copper-cable.png",
        "subgroup": "intermediate-product"
    },
    "small-electric-pole": {
        "name": "small-electric-pole",
        "energy_required": 0.5,
        "ingredients": {
            "wood": 1,
            "copper-cable": 2
        },
        "results": {
            "small-electric-pole": 2
        },
        "icon": "__base__/graphics/icons/small-electric-pole.png",
        "subgroup": "energy-pipe-distribution"
    },
    "pistol": {
        "name": "pistol",
        "energy_required": 5.0,
        "ingredients": {
            "copper-plate": 5,
            "iron-plate": 5
        },
        "results": {
            "pistol": 1
        },
        "icon": "__base__/graphics/icons/pistol.png",
        "subgroup": "gun"
    },
    "submachine-gun": {
        "name": "submachine-gun",
        "energy_required": 10.0,
        "ingredients": {
            "iron-gear-wheel": 10,
            "copper-plate": 5,
            "iron-plate": 10
        },
        "results": {
            "submachine-gun": 1
        },
        "icon": "__base__/graphics/icons/submachine-gun.png",
        "subgroup": "gun"
    },
    "firearm-magazine": {
        "name": "firearm-magazine",
        "energy_required": 1.0,
        "ingredients": {
            "iron-plate": 4
        },
        "results": {
            "firearm-magazine": 1
        },
        "icon": "__base__/graphics/icons/firearm-magazine.png",
        "subgroup": "ammo"
    },
    "light-armor": {
        "name": "light-armor",
        "energy_required": 3.0,
        "ingredients": {
            "iron-plate": 40
        },
        "results": {
            "light-armor": 1
        },
        "icon": "__base__/graphics/icons/light-armor.png",
        "subgroup": "armor"
    },
    "radar": {
        "name": "radar",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 5,
            "iron-gear-wheel": 5,
            "iron-plate": 10
        },
        "results": {
            "radar": 1
        },
        "icon": "__base__/graphics/icons/radar.png",
        "subgroup": "defensive-structure"
    },
    "small-lamp": {
        "name": "small-lamp",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 1,
            "copper-cable": 3,
            "iron-plate": 1
        },
        "results": {
            "small-lamp": 1
        },
        "icon": "__base__/graphics/icons/small-lamp.png",
        "subgroup": "circuit-network"
    },
    "pipe-to-ground": {
        "name": "pipe-to-ground",
        "energy_required": 0.5,
        "ingredients": {
            "pipe": 10,
            "iron-plate": 5
        },
        "results": {
            "pipe-to-ground": 2
        },
        "icon": "__base__/graphics/icons/pipe-to-ground.png",
        "subgroup": "energy-pipe-distribution"
    },
    "assembling-machine-1": {
        "name": "assembling-machine-1",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 3,
            "iron-gear-wheel": 5,
            "iron-plate": 9
        },
        "results": {
            "assembling-machine-1": 1
        },
        "icon": "__base__/graphics/icons/assembling-machine-1.png",
        "subgroup": "production-machine"
    },
    "repair-pack": {
        "name": "repair-pack",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 2,
            "iron-gear-wheel": 2
        },
        "results": {
            "repair-pack": 1
        },
        "icon": "__base__/graphics/icons/repair-pack.png",
        "subgroup": "tool"
    },
    "automation-science-pack": {
        "name": "automation-science-pack",
        "energy_required": 5.0,
        "ingredients": {
            "copper-plate": 1,
            "iron-gear-wheel": 1
        },
        "results": {
            "automation-science-pack": 1
        },
        "icon": "__base__/graphics/icons/automation-science-pack.png",
        "subgroup": "science-pack"
    },
    "logistic-science-pack": {
        "name": "logistic-science-pack",
        "energy_required": 6.0,
        "ingredients": {
            "inserter": 1,
            "transport-belt": 1
        },
        "results": {
            "logistic-science-pack": 1
        },
        "icon": "__base__/graphics/icons/logistic-science-pack.png",
        "subgroup": "science-pack"
    },
    "lab": {
        "name": "lab",
        "energy_required": 2.0,
        "ingredients": {
            "electronic-circuit": 10,
            "iron-gear-wheel": 10,
            "transport-belt": 4
        },
        "results": {
            "lab": 1
        },
        "icon": "__base__/graphics/icons/lab.png",
        "subgroup": "production-machine"
    },
    "stone-wall": {
        "name": "stone-wall",
        "energy_required": 0.5,
        "ingredients": {
            "stone-brick": 5
        },
        "results": {
            "stone-wall": 1
        },
        "icon": "__base__/graphics/icons/wall.png",
        "subgroup": "defensive-structure"
    },
    "assembling-machine-2": {
        "name": "assembling-machine-2",
        "energy_required": 0.5,
        "ingredients": {
            "steel-plate": 2,
            "electronic-circuit": 3,
            "iron-gear-wheel": 5,
            "assembling-machine-1": 1
        },
        "results": {
            "assembling-machine-2": 1
        },
        "icon": "__base__/graphics/icons/assembling-machine-2.png",
        "subgroup": "production-machine"
    },
    "splitter": {
        "name": "splitter",
        "energy_required": 1.0,
        "ingredients": {
            "electronic-circuit": 5,
            "iron-plate": 5,
            "transport-belt": 4
        },
        "results": {
            "splitter": 1
        },
        "icon": "__base__/graphics/icons/splitter.png",
        "subgroup": "belt"
    },
    "underground-belt": {
        "name": "underground-belt",
        "energy_required": 1.0,
        "ingredients": {
            "iron-plate": 10,
            "transport-belt": 5
        },
        "results": {
            "underground-belt": 2
        },
        "icon": "__base__/graphics/icons/underground-belt.png",
        "subgroup": "belt"
    },
    "loader": {
        "name": "loader",
        "energy_required": 1.0,
        "ingredients": {
            "inserter": 5,
            "electronic-circuit": 5,
            "iron-gear-wheel": 5,
            "iron-plate": 5,
            "transport-belt": 5
        },
        "results": {
            "loader": 1
        },
        "icon": "__base__/graphics/icons/loader.png",
        "subgroup": "belt"
    },
    "car": {
        "name": "car",
        "energy_required": 2.0,
        "ingredients": {
            "engine-unit": 8,
            "iron-plate": 20,
            "steel-plate": 5
        },
        "results": {
            "car": 1
        },
        "icon": "__base__/graphics/icons/car.png",
        "subgroup": "transport"
    },
    "engine-unit": {
        "name": "engine-unit",
        "energy_required": 10.0,
        "ingredients": {
            "steel-plate": 1,
            "iron-gear-wheel": 1,
            "pipe": 2
        },
        "results": {
            "engine-unit": 1
        },
        "icon": "__base__/graphics/icons/engine-unit.png",
        "subgroup": "intermediate-product"
    },
    "iron-chest": {
        "name": "iron-chest",
        "energy_required": 0.5,
        "ingredients": {
            "iron-plate": 8
        },
        "results": {
            "iron-chest": 1
        },
        "icon": "__base__/graphics/icons/iron-chest.png",
        "subgroup": "storage"
    },
    "big-electric-pole": {
        "name": "big-electric-pole",
        "energy_required": 0.5,
        "ingredients": {
            "iron-stick": 8,
            "steel-plate": 5,
            "copper-plate": 5
        },
        "results": {
            "big-electric-pole": 1
        },
        "icon": "__base__/graphics/icons/big-electric-pole.png",
        "subgroup": "energy-pipe-distribution"
    },
    "medium-electric-pole": {
        "name": "medium-electric-pole",
        "energy_required": 0.5,
        "ingredients": {
            "iron-stick": 4,
            "steel-plate": 2,
            "copper-plate": 2
        },
        "results": {
            "medium-electric-pole": 1
        },
        "icon": "__base__/graphics/icons/medium-electric-pole.png",
        "subgroup": "energy-pipe-distribution"
    },
    "shotgun": {
        "name": "shotgun",
        "energy_required": 10.0,
        "ingredients": {
            "iron-plate": 15,
            "iron-gear-wheel": 5,
            "copper-plate": 10,
            "wood": 5
        },
        "results": {
            "shotgun": 1
        },
        "icon": "__base__/graphics/icons/shotgun.png",
        "subgroup": "gun"
    },
    "shotgun-shell": {
        "name": "shotgun-shell",
        "energy_required": 3.0,
        "ingredients": {
            "copper-plate": 2,
            "iron-plate": 2
        },
        "results": {
            "shotgun-shell": 1
        },
        "icon": "__base__/graphics/icons/shotgun-shell.png",
        "subgroup": "ammo"
    },
    "piercing-rounds-magazine": {
        "name": "piercing-rounds-magazine",
        "energy_required": 3.0,
        "ingredients": {
            "firearm-magazine": 1,
            "steel-plate": 1,
            "copper-plate": 5
        },
        "results": {
            "piercing-rounds-magazine": 1
        },
        "icon": "__base__/graphics/icons/piercing-rounds-magazine.png",
        "subgroup": "ammo"
    },
    "grenade": {
        "name": "grenade",
        "energy_required": 8.0,
        "ingredients": {
            "iron-plate": 5,
            "coal": 10
        },
        "results": {
            "grenade": 1
        },
        "icon": "__base__/graphics/icons/grenade.png",
        "subgroup": "capsule"
    },
    "steel-furnace": {
        "name": "steel-furnace",
        "energy_required": 3.0,
        "ingredients": {
            "steel-plate": 6,
            "stone-brick": 10
        },
        "results": {
            "steel-furnace": 1
        },
        "icon": "__base__/graphics/icons/steel-furnace.png",
        "subgroup": "smelting-machine"
    },
    "gate": {
        "name": "gate",
        "energy_required": 0.5,
        "ingredients": {
            "stone-wall": 1,
            "steel-plate": 2,
            "electronic-circuit": 2
        },
        "results": {
            "gate": 1
        },
        "icon": "__base__/graphics/icons/gate.png",
        "subgroup": "defensive-structure"
    },
    "heavy-armor": {
        "name": "heavy-armor",
        "energy_required": 8.0,
        "ingredients": {
            "copper-plate": 100,
            "steel-plate": 50
        },
        "results": {
            "heavy-armor": 1
        },
        "icon": "__base__/graphics/icons/heavy-armor.png",
        "subgroup": "armor"
    },
    "steel-chest": {
        "name": "steel-chest",
        "energy_required": 0.5,
        "ingredients": {
            "steel-plate": 8
        },
        "results": {
            "steel-chest": 1
        },
        "icon": "__base__/graphics/icons/steel-chest.png",
        "subgroup": "storage"
    },
    "fast-underground-belt": {
        "name": "fast-underground-belt",
        "energy_required": 2.0,
        "ingredients": {
            "iron-gear-wheel": 40,
            "underground-belt": 2
        },
        "results": {
            "fast-underground-belt": 2
        },
        "icon": "__base__/graphics/icons/fast-underground-belt.png",
        "subgroup": "belt"
    },
    "fast-splitter": {
        "name": "fast-splitter",
        "energy_required": 2.0,
        "ingredients": {
            "splitter": 1,
            "iron-gear-wheel": 10,
            "electronic-circuit": 10
        },
        "results": {
            "fast-splitter": 1
        },
        "icon": "__base__/graphics/icons/fast-splitter.png",
        "subgroup": "belt"
    },
    "concrete": {
        "name": "concrete",
        "energy_required": 10.0,
        "ingredients": {
            "stone-brick": 5,
            "iron-ore": 1,
            "water": 100
        },
        "results": {
            "concrete": 10
        },
        "icon": "__base__/graphics/icons/concrete.png",
        "subgroup": "terrain"
    },
    "hazard-concrete": {
        "name": "hazard-concrete",
        "energy_required": 0.25,
        "ingredients": {
            "concrete": 10
        },
        "results": {
            "hazard-concrete": 10
        },
        "icon": "__base__/graphics/icons/hazard-concrete.png",
        "subgroup": "terrain"
    },
    "refined-concrete": {
        "name": "refined-concrete",
        "energy_required": 15.0,
        "ingredients": {
            "concrete": 20,
            "iron-stick": 8,
            "steel-plate": 1,
            "water": 100
        },
        "results": {
            "refined-concrete": 10
        },
        "icon": "__base__/graphics/icons/refined-concrete.png",
        "subgroup": "terrain"
    },
    "refined-hazard-concrete": {
        "name": "refined-hazard-concrete",
        "energy_required": 0.25,
        "ingredients": {
            "refined-concrete": 10
        },
        "results": {
            "refined-hazard-concrete": 10
        },
        "icon": "__base__/graphics/icons/refined-hazard-concrete.png",
        "subgroup": "terrain"
    },
    "landfill": {
        "name": "landfill",
        "energy_required": 0.5,
        "ingredients": {
            "stone": 20
        },
        "results": {
            "landfill": 1
        },
        "icon": "__base__/graphics/icons/landfill.png",
        "subgroup": "terrain"
    },
    "fast-transport-belt": {
        "name": "fast-transport-belt",
        "energy_required": 0.5,
        "ingredients": {
            "iron-gear-wheel": 5,
            "transport-belt": 1
        },
        "results": {
            "fast-transport-belt": 1
        },
        "icon": "__base__/graphics/icons/fast-transport-belt.png",
        "subgroup": "belt"
    },
    "solar-panel": {
        "name": "solar-panel",
        "energy_required": 10.0,
        "ingredients": {
            "steel-plate": 5,
            "electronic-circuit": 15,
            "copper-plate": 5
        },
        "results": {
            "solar-panel": 1
        },
        "icon": "__base__/graphics/icons/solar-panel.png",
        "subgroup": "energy"
    },
    "rail": {
        "name": "rail",
        "energy_required": 0.5,
        "ingredients": {
            "stone": 1,
            "iron-stick": 1,
            "steel-plate": 1
        },
        "results": {
            "rail": 2
        },
        "icon": "__base__/graphics/icons/rail.png",
        "subgroup": "train-transport"
    },
    "locomotive": {
        "name": "locomotive",
        "energy_required": 4.0,
        "ingredients": {
            "engine-unit": 20,
            "electronic-circuit": 10,
            "steel-plate": 30
        },
        "results": {
            "locomotive": 1
        },
        "icon": "__base__/graphics/icons/locomotive.png",
        "subgroup": "train-transport"
    },
    "cargo-wagon": {
        "name": "cargo-wagon",
        "energy_required": 1.0,
        "ingredients": {
            "iron-gear-wheel": 10,
            "iron-plate": 20,
            "steel-plate": 20
        },
        "results": {
            "cargo-wagon": 1
        },
        "icon": "__base__/graphics/icons/cargo-wagon.png",
        "subgroup": "train-transport"
    },
    "rail-signal": {
        "name": "rail-signal",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 1,
            "iron-plate": 5
        },
        "results": {
            "rail-signal": 1
        },
        "icon": "__base__/graphics/icons/rail-signal.png",
        "subgroup": "train-transport"
    },
    "rail-chain-signal": {
        "name": "rail-chain-signal",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 1,
            "iron-plate": 5
        },
        "results": {
            "rail-chain-signal": 1
        },
        "icon": "__base__/graphics/icons/rail-chain-signal.png",
        "subgroup": "train-transport"
    },
    "train-stop": {
        "name": "train-stop",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 5,
            "iron-plate": 6,
            "iron-stick": 6,
            "steel-plate": 3
        },
        "results": {
            "train-stop": 1
        },
        "icon": "__base__/graphics/icons/train-stop.png",
        "subgroup": "train-transport"
    },
    "copper-plate": {
        "name": "copper-plate",
        "energy_required": 3.2,
        "ingredients": {
            "copper-ore": 1
        },
        "results": {
            "copper-plate": 1
        },
        "icon": "__base__/graphics/icons/copper-plate.png",
        "subgroup": "raw-material"
    },
    "iron-plate": {
        "name": "iron-plate",
        "energy_required": 3.2,
        "ingredients": {
            "iron-ore": 1
        },
        "results": {
            "iron-plate": 1
        },
        "icon": "__base__/graphics/icons/iron-plate.png",
        "subgroup": "raw-material"
    },
    "stone-brick": {
        "name": "stone-brick",
        "energy_required": 3.2,
        "ingredients": {
            "stone": 2
        },
        "results": {
            "stone-brick": 1
        },
        "icon": "__base__/graphics/icons/stone-brick.png",
        "subgroup": "terrain"
    },
    "steel-plate": {
        "name": "steel-plate",
        "energy_required": 16.0,
        "ingredients": {
            "iron-plate": 5
        },
        "results": {
            "steel-plate": 1
        },
        "icon": "__base__/graphics/icons/steel-plate.png",
        "subgroup": "raw-material"
    },
    "arithmetic-combinator": {
        "name": "arithmetic-combinator",
        "energy_required": 0.5,
        "ingredients": {
            "copper-cable": 5,
            "electronic-circuit": 5
        },
        "results": {
            "arithmetic-combinator": 1
        }
    },
    "decider-combinator": {
        "name": "decider-combinator",
        "energy_required": 0.5,
        "ingredients": {
            "copper-cable": 5,
            "electronic-circuit": 5
        },
        "results": {
            "decider-combinator": 1
        },
        "icon": "__base__/graphics/icons/decider-combinator.png",
        "subgroup": "circuit-network"
    },
    "constant-combinator": {
        "name": "constant-combinator",
        "energy_required": 0.5,
        "ingredients": {
            "copper-cable": 5,
            "electronic-circuit": 2
        },
        "results": {
            "constant-combinator": 1
        },
        "icon": "__base__/graphics/icons/constant-combinator.png",
        "subgroup": "circuit-network"
    },
    "power-switch": {
        "name": "power-switch",
        "energy_required": 2.0,
        "ingredients": {
            "iron-plate": 5,
            "copper-cable": 5,
            "electronic-circuit": 2
        },
        "results": {
            "power-switch": 1
        },
        "icon": "__base__/graphics/icons/power-switch.png",
        "subgroup": "circuit-network"
    },
    "programmable-speaker": {
        "name": "programmable-speaker",
        "energy_required": 2.0,
        "ingredients": {
            "iron-plate": 3,
            "iron-stick": 4,
            "copper-cable": 5,
            "electronic-circuit": 4
        },
        "results": {
            "programmable-speaker": 1
        },
        "icon": "__base__/graphics/icons/programmable-speaker.png",
        "subgroup": "circuit-network"
    },
    "red-wire": {
        "name": "red-wire",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 1,
            "copper-cable": 1
        },
        "results": {
            "red-wire": 1
        },
        "icon": "__base__/graphics/icons/red-wire.png",
        "subgroup": "circuit-network"
    },
    "green-wire": {
        "name": "green-wire",
        "energy_required": 0.5,
        "ingredients": {
            "electronic-circuit": 1,
            "copper-cable": 1
        },
        "results": {
            "green-wire": 1
        },
        "icon": "__base__/graphics/icons/green-wire.png",
        "subgroup": "circuit-network"
    },
    "poison-capsule": {
        "name": "poison-capsule",
        "energy_required": 8.0,
        "ingredients": {
            "steel-plate": 3,
            "electronic-circuit": 3,
            "coal": 10
        },
        "results": {
            "poison-capsule": 1
        },
        "icon": "__base__/graphics/icons/poison-capsule.png",
        "subgroup": "capsule"
    },
    "slowdown-capsule": {
        "name": "slowdown-capsule",
        "energy_required": 8.0,
        "ingredients": {
            "steel-plate": 2,
            "electronic-circuit": 2,
            "coal": 5
        },
        "results": {
            "slowdown-capsule": 1
        }
    },
    "cluster-grenade": {
        "name": "cluster-grenade",
        "energy_required": 8.0,
        "ingredients": {
            "grenade": 7,
            "explosives": 5,
            "steel-plate": 5
        },
        "results": {
            "cluster-grenade": 1
        }
    },
    "defender-capsule": {
        "name": "defender-capsule",
        "energy_required": 8.0,
        "ingredients": {
            "piercing-rounds-magazine": 3,
            "electronic-circuit": 3,
            "iron-gear-wheel": 3
        },
        "results": {
            "defender-capsule": 1
        }
    },
    "distractor-capsule": {
        "name": "distractor-capsule",
        "energy_required": 15.0,
        "ingredients": {
            "defender-capsule": 4,
            "advanced-circuit": 3
        },
        "results": {
            "distractor-capsule": 1
        },
        "icon": "__base__/graphics/icons/distractor.png",
        "subgroup": "capsule"
    },
    "destroyer-capsule": {
        "name": "destroyer-capsule",
        "energy_required": 15.0,
        "ingredients": {
            "distractor-capsule": 4,
            "speed-module": 1
        },
        "results": {
            "destroyer-capsule": 1
        },
        "icon": "__base__/graphics/icons/destroyer.png",
        "subgroup": "capsule"
    },
    "cliff-explosives": {
        "name": "cliff-explosives",
        "energy_required": 8.0,
        "ingredients": {
            "explosives": 10,
            "grenade": 1,
            "empty-barrel": 1
        },
        "results": {
            "cliff-explosives": 1
        },
        "icon": "__base__/graphics/icons/cliff-explosives.png",
        "subgroup": "terrain"
    },
    "uranium-rounds-magazine": {
        "name": "uranium-rounds-magazine",
        "energy_required": 10.0,
        "ingredients": {
            "piercing-rounds-magazine": 1,
            "uranium-238": 1
        },
        "results": {
            "uranium-rounds-magazine": 1
        }
    },
    "rocket": {
        "name": "rocket",
        "energy_required": 8.0,
        "ingredients": {
            "electronic-circuit": 1,
            "explosives": 1,
            "iron-plate": 2
        },
        "results": {
            "rocket": 1
        },
        "icon": "__base__/graphics/icons/rocket.png",
        "subgroup": "ammo"
    },
    "explosive-rocket": {
        "name": "explosive-rocket",
        "energy_required": 8.0,
        "ingredients": {
            "rocket": 1,
            "explosives": 2
        },
        "results": {
            "explosive-rocket": 1
        },
        "icon": "__base__/graphics/icons/explosive-rocket.png",
        "subgroup": "ammo"
    },
    "atomic-bomb": {
        "name": "atomic-bomb",
        "energy_required": 50.0,
        "ingredients": {
            "rocket-control-unit": 10,
            "explosives": 10,
            "uranium-235": 30
        },
        "results": {
            "atomic-bomb": 1
        },
        "icon": "__base__/graphics/icons/atomic-bomb.png",
        "subgroup": "ammo"
    },
    "piercing-shotgun-shell": {
        "name": "piercing-shotgun-shell",
        "energy_required": 8.0,
        "ingredients": {
            "shotgun-shell": 2,
            "copper-plate": 5,
            "steel-plate": 2
        },
        "results": {
            "piercing-shotgun-shell": 1
        },
        "icon": "__base__/graphics/icons/piercing-shotgun-shell.png",
        "subgroup": "ammo"
    },
    "cannon-shell": {
        "name": "cannon-shell",
        "energy_required": 8.0,
        "ingredients": {
            "steel-plate": 2,
            "plastic-bar": 2,
            "explosives": 1
        },
        "results": {
            "cannon-shell": 1
        },
        "icon": "__base__/graphics/icons/cannon-shell.png",
        "subgroup": "ammo"
    },
    "explosive-cannon-shell": {
        "name": "explosive-cannon-shell",
        "energy_required": 8.0,
        "ingredients": {
            "steel-plate": 2,
            "plastic-bar": 2,
            "explosives": 2
        },
        "results": {
            "explosive-cannon-shell": 1
        },
        "icon": "__base__/graphics/icons/explosive-cannon-shell.png",
        "subgroup": "ammo"
    },
    "uranium-cannon-shell": {
        "name": "uranium-cannon-shell",
        "energy_required": 12.0,
        "ingredients": {
            "cannon-shell": 1,
            "uranium-238": 1
        },
        "results": {
            "uranium-cannon-shell": 1
        },
        "icon": "__base__/graphics/icons/uranium-cannon-shell.png",
        "subgroup": "ammo"
    },
    "explosive-uranium-cannon-shell": {
        "name": "explosive-uranium-cannon-shell",
        "energy_required": 12.0,
        "ingredients": {
            "explosive-cannon-shell": 1,
            "uranium-238": 1
        },
        "results": {
            "explosive-uranium-cannon-shell": 1
        },
        "icon": "__base__/graphics/icons/explosive-uranium-cannon-shell.png",
        "subgroup": "ammo"
    },
    "artillery-shell": {
        "name": "artillery-shell",
        "energy_required": 15.0,
        "ingredients": {
            "explosive-cannon-shell": 4,
            "radar": 1,
            "explosives": 8
        },
        "results": {
            "artillery-shell": 1
        },
        "icon": "__base__/graphics/icons/artillery-shell.png",
        "subgroup": "ammo"
    },
    "flamethrower-ammo": {
        "name": "flamethrower-ammo",
        "energy_required": 6.0,
        "ingredients": {
            "steel-plate": 5,
            "crude-oil": 100
        },
        "results": {
            "flamethrower-ammo": 1
        },
        "icon": "__base__/graphics/icons/flamethrower-ammo.png",
        "subgroup": "ammo"
    },
    "express-transport-belt": {
        "name": "express-transport-belt",
        "energy_required": 0.5,
        "ingredients": {
            "iron-gear-wheel": 10,
            "fast-transport-belt": 1,
            "lubricant": 20
        },
        "results": {
            "express-transport-belt": 1
        },
        "icon": "__base__/graphics/icons/express-transport-belt.png",
        "subgroup": "belt"
    },
    "assembling-machine-3": {
        "name": "assembling-machine-3",
        "energy_required": 0.5,
        "ingredients": {
            "speed-module": 4,
            "assembling-machine-2": 2
        },
        "results": {
            "assembling-machine-3": 1
        },
        "icon": "__base__/graphics/icons/assembling-machine-3.png",
        "subgroup": "production-machine"
    },
    "tank": {
        "name": "tank",
        "energy_required": 5.0,
        "ingredients": {
            "engine-unit": 32,
            "steel-plate": 50,
            "iron-gear-wheel": 15,
            "advanced-circuit": 10
        },
        "results": {
            "tank": 1
        },
        "icon": "__base__/graphics/icons/tank.png",
        "subgroup": "transport"
    },
    "spidertron": {
        "name": "spidertron",
        "energy_required": 10.0,
        "ingredients": {
            "exoskeleton-equipment": 4,
            "fusion-reactor-equipment": 2,
            "rocket-launcher": 4,
            "rocket-control-unit": 16,
            "low-density-structure": 150,
            "radar": 2,
            "effectivity-module-3": 2,
            "raw-fish": 1
        },
        "results": {
            "spidertron": 1
        },
        "icon": "__base__/graphics/icons/spidertron.png",
        "subgroup": "transport"
    },
    "spidertron-remote": {
        "name": "spidertron-remote",
        "energy_required": 0.5,
        "ingredients": {
            "rocket-control-unit": 1,
            "radar": 1
        },
        "results": {
            "spidertron-remote": 1
        },
        "icon": "__base__/graphics/icons/spidertron-remote.png",
        "subgroup": "transport"
    },
    "fluid-wagon": {
        "name": "fluid-wagon",
        "energy_required": 1.5,
        "ingredients": {
            "iron-gear-wheel": 10,
            "steel-plate": 16,
            "pipe": 8,
            "storage-tank": 1
        },
        "results": {
            "fluid-wagon": 1
        },
        "icon": "__base__/graphics/icons/fluid-wagon.png",
        "subgroup": "train-transport"
    },
    "artillery-wagon": {
        "name": "artillery-wagon",
        "energy_required": 4.0,
        "ingredients": {
            "engine-unit": 64,
            "iron-gear-wheel": 10,
            "steel-plate": 40,
            "pipe": 16,
            "advanced-circuit": 20
        },
        "results": {
            "artillery-wagon": 1
        },
        "icon": "__base__/graphics/icons/artillery-wagon.png",
        "subgroup": "train-transport"
    },
    "modular-armor": {
        "name": "modular-armor",
        "energy_required": 15.0,
        "ingredients": {
            "advanced-circuit": 30,
            "steel-plate": 50
        },
        "results": {
            "modular-armor": 1
        }
    },
    "power-armor": {
        "name": "power-armor",
        "energy_required": 20.0,
        "ingredients": {
            "processing-unit": 40,
            "electric-engine-unit": 20,
            "steel-plate": 40
        },
        "results": {
            "power-armor": 1
        },
        "icon": "__base__/graphics/icons/power-armor.png",
        "subgroup": "armor"
    },
    "power-armor-mk2": {
        "name": "power-armor-mk2",
        "energy_required": 25.0,
        "ingredients": {
            "effectivity-module-2": 25,
            "speed-module-2": 25,
            "processing-unit": 60,
            "electric-engine-unit": 40,
            "low-density-structure": 30
        },
        "results": {
            "power-armor-mk2": 1
        },
        "icon": "__base__/graphics/icons/power-armor-mk2.png",
        "subgroup": "armor"
    },
    "flamethrower": {
        "name": "flamethrower",
        "energy_required": 10.0,
        "ingredients": {
            "steel-plate": 5,
            "iron-gear-wheel": 10
        },
        "results": {
            "flamethrower": 1
        },
        "icon": "__base__/graphics/icons/flamethrower.png",
        "subgroup": "gun"
    },
    "land-mine": {
        "name": "land-mine",
        "energy_required": 5.0,
        "ingredients": {
            "steel-plate": 1,
            "explosives": 2
        },
        "results": {
            "land-mine": 4
        },
        "icon": "__base__/graphics/icons/land-mine.png",
        "subgroup": "gun"
    },
    "rocket-launcher": {
        "name": "rocket-launcher",
        "energy_required": 10.0,
        "ingredients": {
            "iron-plate": 5,
            "iron-gear-wheel": 5,
            "electronic-circuit": 5
        },
        "results": {
            "rocket-launcher": 1
        },
        "icon": "__base__/graphics/icons/rocket-launcher.png",
        "subgroup": "gun"
    },
    "combat-shotgun": {
        "name": "combat-shotgun",
        "energy_required": 10.0,
        "ingredients": {
            "steel-plate": 15,
            "iron-gear-wheel": 5,
            "copper-plate": 10,
            "wood": 10
        },
        "results": {
            "combat-shotgun": 1
        },
        "icon": "__base__/graphics/icons/combat-shotgun.png",
        "subgroup": "gun"
    },
    "chemical-science-pack": {
        "name": "chemical-science-pack",
        "energy_required": 24.0,
        "ingredients": {
            "engine-unit": 2,
            "advanced-circuit": 3,
            "sulfur": 1
        },
        "results": {
            "chemical-science-pack": 2
        },
        "icon": "__base__/graphics/icons/chemical-science-pack.png",
        "subgroup": "science-pack"
    },
    "military-science-pack": {
        "name": "military-science-pack",
        "energy_required": 10.0,
        "ingredients": {
            "piercing-rounds-magazine": 1,
            "grenade": 1,
            "stone-wall": 2
        },
        "results": {
            "military-science-pack": 2
        },
        "icon": "__base__/graphics/icons/military-science-pack.png",
        "subgroup": "science-pack"
    },
    "production-science-pack": {
        "name": "production-science-pack",
        "energy_required": 21.0,
        "ingredients": {
            "electric-furnace": 1,
            "productivity-module": 1,
            "rail": 30
        },
        "results": {
            "production-science-pack": 3
        },
        "icon": "__base__/graphics/icons/production-science-pack.png",
        "subgroup": "science-pack"
    },
    "utility-science-pack": {
        "name": "utility-science-pack",
        "energy_required": 21.0,
        "ingredients": {
            "low-density-structure": 3,
            "processing-unit": 2,
            "flying-robot-frame": 1
        },
        "results": {
            "utility-science-pack": 3
        },
        "icon": "__base__/graphics/icons/utility-science-pack.png",
        "subgroup": "science-pack"
    },
    "express-underground-belt": {
        "name": "express-underground-belt",
        "energy_required": 2.0,
        "ingredients": {
            "iron-gear-wheel": 80,
            "fast-underground-belt": 2,
            "lubricant": 40
        },
        "results": {
            "express-underground-belt": 2
        },
        "icon": "__base__/graphics/icons/express-underground-belt.png",
        "subgroup": "belt"
    },
    "fast-loader": {
        "name": "fast-loader",
        "energy_required": 3.0,
        "ingredients": {
            "fast-transport-belt": 5,
            "loader": 1
        },
        "results": {
            "fast-loader": 1
        },
        "icon": "__base__/graphics/icons/fast-loader.png",
        "subgroup": "belt"
    },
    "express-loader": {
        "name": "express-loader",
        "energy_required": 10.0,
        "ingredients": {
            "express-transport-belt": 5,
            "fast-loader": 1
        },
        "results": {
            "express-loader": 1
        },
        "icon": "__base__/graphics/icons/express-loader.png",
        "subgroup": "belt"
    },
    "express-splitter": {
        "name": "express-splitter",
        "energy_required": 2.0,
        "ingredients": {
            "fast-splitter": 1,
            "iron-gear-wheel": 10,
            "advanced-circuit": 10,
            "lubricant": 80
        },
        "results": {
            "express-splitter": 1
        },
        "icon": "__base__/graphics/icons/express-splitter.png",
        "subgroup": "belt"
    },
    "advanced-circuit": {
        "name": "advanced-circuit",
        "energy_required": 6.0,
        "ingredients": {
            "electronic-circuit": 2,
            "plastic-bar": 2,
            "copper-cable": 4
        },
        "results": {
            "advanced-circuit": 1
        },
        "icon": "__base__/graphics/icons/advanced-circuit.png",
        "subgroup": "intermediate-product"
    },
    "processing-unit": {
        "name": "processing-unit",
        "energy_required": 10.0,
        "ingredients": {
            "electronic-circuit": 20,
            "advanced-circuit": 2,
            "sulfuric-acid": 5
        },
        "results": {
            "processing-unit": 1
        },
        "icon": "__base__/graphics/icons/processing-unit.png",
        "subgroup": "intermediate-product"
    },
    "logistic-robot": {
        "name": "logistic-robot",
        "energy_required": 0.5,
        "ingredients": {
            "flying-robot-frame": 1,
            "advanced-circuit": 2
        },
        "results": {
            "logistic-robot": 1
        },
        "icon": "__base__/graphics/icons/logistic-robot.png",
        "subgroup": "logistic-network"
    },
    "construction-robot": {
        "name": "construction-robot",
        "energy_required": 0.5,
        "ingredients": {
            "flying-robot-frame": 1,
            "electronic-circuit": 2
        },
        "results": {
            "construction-robot": 1
        },
        "icon": "__base__/graphics/icons/construction-robot.png",
        "subgroup": "logistic-network"
    },
    "logistic-chest-passive-provider": {
        "name": "logistic-chest-passive-provider",
        "energy_required": 0.5,
        "ingredients": {
            "steel-chest": 1,
            "electronic-circuit": 3,
            "advanced-circuit": 1
        },
        "results": {
            "logistic-chest-passive-provider": 1
        },
        "icon": "__base__/graphics/icons/logistic-chest-passive-provider.png",
        "subgroup": "logistic-network"
    },
    "logistic-chest-active-provider": {
        "name": "logistic-chest-active-provider",
        "energy_required": 0.5,
        "ingredients": {
            "steel-chest": 1,
            "electronic-circuit": 3,
            "advanced-circuit": 1
        },
        "results": {
            "logistic-chest-active-provider": 1
        },
        "icon": "__base__/graphics/icons/logistic-chest-active-provider.png",
        "subgroup": "logistic-network"
    },
    "logistic-chest-storage": {
        "name": "logistic-chest-storage",
        "energy_required": 0.5,
        "ingredients": {
            "steel-chest": 1,
            "electronic-circuit": 3,
            "advanced-circuit": 1
        },
        "results": {
            "logistic-chest-storage": 1
        },
        "icon": "__base__/graphics/icons/logistic-chest-storage.png",
        "subgroup": "logistic-network"
    },
    "logistic-chest-buffer": {
        "name": "logistic-chest-buffer",
        "energy_required": 0.5,
        "ingredients": {
            "steel-chest": 1,
            "electronic-circuit": 3,
            "advanced-circuit": 1
        },
        "results": {
            "logistic-chest-buffer": 1
        },
        "icon": "__base__/graphics/icons/logistic-chest-buffer.png",
        "subgroup": "logistic-network"
    },
    "logistic-chest-requester": {
        "name": "logistic-chest-requester",
        "energy_required": 0.5,
        "ingredients": {
            "steel-chest": 1,
            "electronic-circuit": 3,
            "advanced-circuit": 1
        },
        "results": {
            "logistic-chest-requester": 1
        },
        "icon": "__base__/graphics/icons/logistic-chest-requester.png",
        "subgroup": "logistic-network"
    },
    "rocket-silo": {
        "name": "rocket-silo",
        "energy_required": 30.0,
        "ingredients": {
            "steel-plate": 1000,
            "concrete": 1000,
            "pipe": 100,
            "processing-unit": 200,
            "electric-engine-unit": 200
        },
        "results": {
            "rocket-silo": 1
        },
        "icon": "__base__/graphics/icons/rocket-silo.png",
        "subgroup": "space-related"
    },
    "roboport": {
        "name": "roboport",
        "energy_required": 5.0,
        "ingredients": {
            "steel-plate": 45,
            "iron-gear-wheel": 45,
            "advanced-circuit": 45
        },
        "results": {
            "roboport": 1
        },
        "icon": "__base__/graphics/icons/roboport.png",
        "subgroup": "logistic-network"
    },
    "substation": {
        "name": "substation",
        "energy_required": 0.5,
        "ingredients": {
            "steel-plate": 10,
            "advanced-circuit": 5,
            "copper-plate": 5
        },
        "results": {
            "substation": 1
        },
        "icon": "__base__/graphics/icons/substation.png",
        "subgroup": "energy-pipe-distribution"
    },
    "accumulator": {
        "name": "accumulator",
        "energy_required": 10.0,
        "ingredients": {
            "iron-plate": 2,
            "battery": 5
        },
        "results": {
            "accumulator": 1
        },
        "icon": "__base__/graphics/icons/accumulator.png",
        "subgroup": "energy"
    },
    "electric-furnace": {
        "name": "electric-furnace",
        "energy_required": 5.0,
        "ingredients": {
            "steel-plate": 10,
            "advanced-circuit": 5,
            "stone-brick": 10
        },
        "results": {
            "electric-furnace": 1
        },
        "icon": "__base__/graphics/icons/electric-furnace.png",
        "subgroup": "smelting-machine"
    },
    "beacon": {
        "name": "beacon",
        "energy_required": 15.0,
        "ingredients": {
            "electronic-circuit": 20,
            "advanced-circuit": 20,
            "steel-plate": 10,
            "copper-cable": 10
        },
        "results": {
            "beacon": 1
        },
        "icon": "__base__/graphics/icons/beacon.png",
        "subgroup": "module"
    },
    "pumpjack": {
        "name": "pumpjack",
        "energy_required": 5.0,
        "ingredients": {
            "steel-plate": 5,
            "iron-gear-wheel": 10,
            "electronic-circuit": 5,
            "pipe": 10
        },
        "results": {
            "pumpjack": 1
        },
        "icon": "__base__/graphics/icons/pumpjack.png",
        "subgroup": "extraction-machine"
    },
    "oil-refinery": {
        "name": "oil-refinery",
        "energy_required": 8.0,
        "ingredients": {
            "steel-plate": 15,
            "iron-gear-wheel": 10,
            "stone-brick": 10,
            "electronic-circuit": 10,
            "pipe": 10
        },
        "results": {
            "oil-refinery": 1
        },
        "icon": "__base__/graphics/icons/oil-refinery.png",
        "subgroup": "production-machine"
    },
    "electric-engine-unit": {
        "name": "electric-engine-unit",
        "energy_required": 10.0,
        "ingredients": {
            "engine-unit": 1,
            "lubricant": 15,
            "electronic-circuit": 2
        },
        "results": {
            "electric-engine-unit": 1
        },
        "icon": "__base__/graphics/icons/electric-engine-unit.png",
        "subgroup": "intermediate-product"
    },
    "flying-robot-frame": {
        "name": "flying-robot-frame",
        "energy_required": 20.0,
        "ingredients": {
            "electric-engine-unit": 1,
            "battery": 2,
            "steel-plate": 1,
            "electronic-circuit": 3
        },
        "results": {
            "flying-robot-frame": 1
        },
        "icon": "__base__/graphics/icons/flying-robot-frame.png",
        "subgroup": "intermediate-product"
    },
    "explosives": {
        "name": "explosives",
        "energy_required": 4.0,
        "ingredients": {
            "sulfur": 1,
            "coal": 1,
            "water": 10
        },
        "results": {
            "explosives": 2
        },
        "icon": "__base__/graphics/icons/explosives.png",
        "subgroup": "raw-material"
    },
    "battery": {
        "name": "battery",
        "energy_required": 4.0,
        "ingredients": {
            "sulfuric-acid": 20,
            "iron-plate": 1,
            "copper-plate": 1
        },
        "results": {
            "battery": 1
        },
        "icon": "__base__/graphics/icons/battery.png",
        "subgroup": "raw-material"
    },
    "storage-tank": {
        "name": "storage-tank",
        "energy_required": 3.0,
        "ingredients": {
            "iron-plate": 20,
            "steel-plate": 5
        },
        "results": {
            "storage-tank": 1
        },
        "icon": "__base__/graphics/icons/storage-tank.png",
        "subgroup": "storage"
    },
    "pump": {
        "name": "pump",
        "energy_required": 2.0,
        "ingredients": {
            "engine-unit": 1,
            "steel-plate": 1,
            "pipe": 1
        },
        "results": {
            "pump": 1
        },
        "icon": "__base__/graphics/icons/pump.png",
        "subgroup": "energy-pipe-distribution"
    },
    "chemical-plant": {
        "name": "chemical-plant",
        "energy_required": 5.0,
        "ingredients": {
            "steel-plate": 5,
            "iron-gear-wheel": 5,
            "electronic-circuit": 5,
            "pipe": 5
        },
        "results": {
            "chemical-plant": 1
        },
        "icon": "__base__/graphics/icons/chemical-plant.png",
        "subgroup": "production-machine"
    },
    "low-density-structure": {
        "name": "low-density-structure",
        "energy_required": 20.0,
        "ingredients": {
            "steel-plate": 2,
            "copper-plate": 20,
            "plastic-bar": 5
        },
        "results": {
            "low-density-structure": 1
        },
        "icon": "__base__/graphics/icons/low-density-structure.png",
        "subgroup": "intermediate-product"
    },
    "rocket-fuel": {
        "name": "rocket-fuel",
        "energy_required": 30.0,
        "ingredients": {
            "solid-fuel": 10,
            "light-oil": 10
        },
        "results": {
            "rocket-fuel": 1
        },
        "icon": "__base__/graphics/icons/rocket-fuel.png",
        "subgroup": "intermediate-product"
    },
    "rocket-control-unit": {
        "name": "rocket-control-unit",
        "energy_required": 30.0,
        "ingredients": {
            "processing-unit": 1,
            "speed-module": 1
        },
        "results": {
            "rocket-control-unit": 1
        },
        "icon": "__base__/graphics/icons/rocket-control-unit.png",
        "subgroup": "intermediate-product"
    },
    "rocket-part": {
        "name": "rocket-part",
        "energy_required": 3.0,
        "ingredients": {
            "rocket-control-unit": 10,
            "low-density-structure": 10,
            "rocket-fuel": 10
        },
        "results": {
            "rocket-part": 1
        },
        "icon": "__base__/graphics/icons/rocket-part.png",
        "subgroup": "intermediate-product"
    },
    "satellite": {
        "name": "satellite",
        "energy_required": 5.0,
        "ingredients": {
            "low-density-structure": 100,
            "solar-panel": 100,
            "accumulator": 100,
            "radar": 5,
            "processing-unit": 100,
            "rocket-fuel": 50
        },
        "results": {
            "satellite": 1
        },
        "icon": "__base__/graphics/icons/satellite.png",
        "subgroup": "space-related"
    },
    "electric-energy-interface": {
        "name": "electric-energy-interface",
        "energy_required": 0.5,
        "ingredients": {
            "iron-plate": 2,
            "electronic-circuit": 5
        },
        "results": {
            "electric-energy-interface": 1
        },
        "subgroup": "other"
    },
    "nuclear-reactor": {
        "name": "nuclear-reactor",
        "energy_required": 8.0,
        "ingredients": {
            "concrete": 500,
            "steel-plate": 500,
            "advanced-circuit": 500,
            "copper-plate": 500
        },
        "results": {
            "nuclear-reactor": 1
        },
        "icon": "__base__/graphics/icons/nuclear-reactor.png",
        "subgroup": "energy"
    },
    "centrifuge": {
        "name": "centrifuge",
        "energy_required": 4.0,
        "ingredients": {
            "concrete": 100,
            "steel-plate": 50,
            "advanced-circuit": 100,
            "iron-gear-wheel": 100
        },
        "results": {
            "centrifuge": 1
        },
        "icon": "__base__/graphics/icons/centrifuge.png",
        "subgroup": "production-machine"
    },
    "kovarex-enrichment-process": {
        "name": "kovarex-enrichment-process",
        "energy_required": 60.0,
        "ingredients": {
            "uranium-235": 40,
            "uranium-238": 5
        },
        "results": {
            "uranium-235": 41,
            "uranium-238": 2
        }
    },
    "nuclear-fuel": {
        "name": "nuclear-fuel",
        "energy_required": 90.0,
        "ingredients": {
            "uranium-235": 1,
            "rocket-fuel": 1
        },
        "results": {
            "nuclear-fuel": 1
        },
        "icon": "__base__/graphics/icons/nuclear-fuel.png",
        "subgroup": "intermediate-product"
    },
    "nuclear-fuel-reprocessing": {
        "name": "nuclear-fuel-reprocessing",
        "energy_required": 60.0,
        "ingredients": {
            "used-up-uranium-fuel-cell": 5
        },
        "results": {
            "uranium-238": 3
        }
    },
    "uranium-fuel-cell": {
        "name": "uranium-fuel-cell",
        "energy_required": 10.0,
        "ingredients": {
            "iron-plate": 10,
            "uranium-235": 1,
            "uranium-238": 19
        },
        "results": {
            "uranium-fuel-cell": 10
        },
        "icon": "__base__/graphics/icons/uranium-fuel-cell.png",
        "subgroup": "intermediate-product"
    },
    "heat-exchanger": {
        "name": "heat-exchanger",
        "energy_required": 3.0,
        "ingredients": {
            "steel-plate": 10,
            "copper-plate": 100,
            "pipe": 10
        },
        "results": {
            "heat-exchanger": 1
        },
        "icon": "__base__/graphics/icons/heat-boiler.png",
        "subgroup": "energy"
    },
    "heat-pipe": {
        "name": "heat-pipe",
        "energy_required": 1.0,
        "ingredients": {
            "steel-plate": 10,
            "copper-plate": 20
        },
        "results": {
            "heat-pipe": 1
        },
        "icon": "__base__/graphics/icons/heat-pipe.png",
        "subgroup": "energy"
    },
    "steam-turbine": {
        "name": "steam-turbine",
        "energy_required": 3.0,
        "ingredients": {
            "iron-gear-wheel": 50,
            "copper-plate": 50,
            "pipe": 20
        },
        "results": {
            "steam-turbine": 1
        },
        "icon": "__base__/graphics/icons/steam-turbine.png",
        "subgroup": "energy"
    },
    "crude-oil": {
        "name": "crude-oil",
        "energy_required": "",
        "ingredients": "",
        "results": ""
    },
    "water": {
        "name": "water",
        "energy_required": "",
        "ingredients": "",
        "results": ""
    },
    "coal": {
        "name": "coal",
        "energy_required": "",
        "ingredients": "",
        "results": "",
        "icon": "__base__/graphics/icons/coal.png",
        "subgroup": "raw-resource"
    },
    "heavy-oil": {
        "name": "heavy-oil",
        "energy_required": "",
        "ingredients": "",
        "results": ""
    },
    "steam": {
        "name": "steam",
        "energy_required": "",
        "ingredients": "",
        "results": ""
    },
    "light-oil": {
        "name": "light-oil",
        "energy_required": "",
        "ingredients": "",
        "results": ""
    },
    "petroleum-gas": {
        "name": "petroleum-gas",
        "energy_required": "",
        "ingredients": "",
        "results": ""
    },
    "wood": {
        "name": "wood",
        "energy_required": "",
        "ingredients": "",
        "results": "",
        "icon": "__base__/graphics/icons/wood.png",
        "subgroup": "raw-resource"
    },
    "stone": {
        "name": "stone",
        "energy_required": "",
        "ingredients": "",
        "results": "",
        "icon": "__base__/graphics/icons/stone.png",
        "subgroup": "raw-resource"
    },
    "iron-ore": {
        "name": "iron-ore",
        "energy_required": "",
        "ingredients": "",
        "results": "",
        "icon": "__base__/graphics/icons/iron-ore.png",
        "subgroup": "raw-resource"
    },
    "copper-ore": {
        "name": "copper-ore",
        "energy_required": "",
        "ingredients": "",
        "results": "",
        "icon": "__base__/graphics/icons/copper-ore.png",
        "subgroup": "raw-resource"
    },
    "uranium-238": {
        "name": "uranium-238",
        "energy_required": "",
        "ingredients": "",
        "results": "",
        "icon": "__base__/graphics/icons/uranium-238.png",
        "subgroup": "intermediate-product"
    },
    "uranium-235": {
        "name": "uranium-235",
        "energy_required": "",
        "ingredients": "",
        "results": "",
        "icon": "__base__/graphics/icons/uranium-235.png",
        "subgroup": "intermediate-product"
    },
    "raw-fish": {
        "name": "raw-fish",
        "energy_required": "",
        "ingredients": "",
        "results": "",
        "icon": "__base__/graphics/icons/fish.png",
        "subgroup": "raw-resource"
    },
    "solid-fuel": {
        "name": "solid-fuel",
        "energy_required": "",
        "ingredients": "",
        "results": "",
        "icon": "__base__/graphics/icons/solid-fuel.png",
        "subgroup": "raw-material"
    },
    "used-up-uranium-fuel-cell": {
        "name": "used-up-uranium-fuel-cell",
        "energy_required": "",
        "ingredients": "",
        "results": "",
        "icon": "__base__/graphics/icons/used-up-uranium-fuel-cell.png",
        "subgroup": "intermediate-product"
    }
}
