item_dict = {
    "stone-brick": {
        "type": "item_dict",
        "name": "stone-brick",
        "icon": "__base__/graphics/icons/stone-brick.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "terrain",
        "order": "a[stone-brick]",
        "stack_size": 100,
        "place_as_tile": {
            "result": "stone-path",
            "condition_size": 1,
            "condition": [
                "water-tile"
            ]
        }
    },
    "wood": {
        "type": "item_dict",
        "name": "wood",
        "icon": "__base__/graphics/icons/wood.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "fuel_value": "2MJ",
        "fuel_category": "chemical",
        "subgroup": "raw-resource",
        "order": "a[wood]",
        "stack_size": 100
    },
    "coal": {
        "type": "item_dict",
        "name": "coal",
        "icon": "__base__/graphics/icons/coal.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "dark_background_icon": "__base__/graphics/icons/coal-dark-background.png",
        "pictures": [
            {
                "size": 64,
                "filename": "__base__/graphics/icons/coal.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/coal-1.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/coal-2.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/coal-3.png",
                "scale": 0.25,
                "mipmap_count": 4
            }
        ],
        "fuel_category": "chemical",
        "fuel_value": "4MJ",
        "subgroup": "raw-resource",
        "order": "b[coal]",
        "stack_size": 50
    },
    "stone": {
        "type": "item_dict",
        "name": "stone",
        "icon": "__base__/graphics/icons/stone.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "pictures": [
            {
                "size": 64,
                "filename": "__base__/graphics/icons/stone.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/stone-1.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/stone-2.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/stone-3.png",
                "scale": 0.25,
                "mipmap_count": 4
            }
        ],
        "subgroup": "raw-resource",
        "order": "d[stone]",
        "stack_size": 50
    },
    "iron-ore": {
        "type": "item_dict",
        "name": "iron-ore",
        "icon": "__base__/graphics/icons/iron-ore.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "pictures": [
            {
                "size": 64,
                "filename": "__base__/graphics/icons/iron-ore.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/iron-ore-1.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/iron-ore-2.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/iron-ore-3.png",
                "scale": 0.25,
                "mipmap_count": 4
            }
        ],
        "subgroup": "raw-resource",
        "order": "e[iron-ore]",
        "stack_size": 50
    },
    "copper-ore": {
        "type": "item_dict",
        "name": "copper-ore",
        "icon": "__base__/graphics/icons/copper-ore.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "pictures": [
            {
                "size": 64,
                "filename": "__base__/graphics/icons/copper-ore.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/copper-ore-1.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/copper-ore-2.png",
                "scale": 0.25,
                "mipmap_count": 4
            },
            {
                "size": 64,
                "filename": "__base__/graphics/icons/copper-ore-3.png",
                "scale": 0.25,
                "mipmap_count": 4
            }
        ],
        "subgroup": "raw-resource",
        "order": "f[copper-ore]",
        "stack_size": 50
    },
    "iron-plate": {
        "type": "item_dict",
        "name": "iron-plate",
        "icon": "__base__/graphics/icons/iron-plate.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "raw-material",
        "order": "b[iron-plate]",
        "stack_size": 100
    },
    "copper-plate": {
        "type": "item_dict",
        "name": "copper-plate",
        "icon": "__base__/graphics/icons/copper-plate.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "raw-material",
        "order": "c[copper-plate]",
        "stack_size": 100
    },
    "copper-cable": {
        "type": "item_dict",
        "name": "copper-cable",
        "icon": "__base__/graphics/icons/copper-cable.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "a[copper-cable]",
        "stack_size": 200,
        "wire_count": 1
    },
    "iron-stick": {
        "type": "item_dict",
        "name": "iron-stick",
        "icon": "__base__/graphics/icons/iron-stick.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "b[iron-stick]",
        "stack_size": 100
    },
    "iron-gear-wheel": {
        "type": "item_dict",
        "name": "iron-gear-wheel",
        "icon": "__base__/graphics/icons/iron-gear-wheel.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "c[iron-gear-wheel]",
        "stack_size": 100
    },
    "electronic-circuit": {
        "type": "item_dict",
        "name": "electronic-circuit",
        "icon": "__base__/graphics/icons/electronic-circuit.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "e[electronic-circuit]",
        "stack_size": 200
    },
    "wooden-chest": {
        "type": "item_dict",
        "name": "wooden-chest",
        "icon": "__base__/graphics/icons/wooden-chest.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "storage",
        "order": "a[items]-a[wooden-chest]",
        "place_result": "wooden-chest",
        "stack_size": 50
    },
    "stone-furnace": {
        "type": "item_dict",
        "name": "stone-furnace",
        "icon": "__base__/graphics/icons/stone-furnace.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "smelting-machine",
        "order": "a[stone-furnace]",
        "place_result": "stone-furnace",
        "stack_size": 50
    },
    "burner-mining-drill": {
        "type": "item_dict",
        "name": "burner-mining-drill",
        "icon": "__base__/graphics/icons/burner-mining-drill.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "extraction-machine",
        "order": "a[items]-a[burner-mining-drill]",
        "place_result": "burner-mining-drill",
        "stack_size": 50
    },
    "electric-mining-drill": {
        "type": "item_dict",
        "name": "electric-mining-drill",
        "icon": "__base__/graphics/icons/electric-mining-drill.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "extraction-machine",
        "order": "a[items]-b[electric-mining-drill]",
        "place_result": "electric-mining-drill",
        "stack_size": 50
    },
    "burner-inserter": {
        "type": "item_dict",
        "name": "burner-inserter",
        "icon": "__base__/graphics/icons/burner-inserter.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "inserter",
        "order": "a[burner-inserter]",
        "place_result": "burner-inserter",
        "stack_size": 50
    },
    "inserter": {
        "type": "item_dict",
        "name": "inserter",
        "icon": "__base__/graphics/icons/inserter.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "inserter",
        "order": "b[inserter]",
        "place_result": "inserter",
        "stack_size": 50
    },
    "fast-inserter": {
        "type": "item_dict",
        "name": "fast-inserter",
        "icon": "__base__/graphics/icons/fast-inserter.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "inserter",
        "order": "d[fast-inserter]",
        "place_result": "fast-inserter",
        "stack_size": 50
    },
    "filter-inserter": {
        "type": "item_dict",
        "name": "filter-inserter",
        "icon": "__base__/graphics/icons/filter-inserter.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "inserter",
        "order": "e[filter-inserter]",
        "place_result": "filter-inserter",
        "stack_size": 50
    },
    "long-handed-inserter": {
        "type": "item_dict",
        "name": "long-handed-inserter",
        "icon": "__base__/graphics/icons/long-handed-inserter.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "inserter",
        "order": "c[long-handed-inserter]",
        "place_result": "long-handed-inserter",
        "stack_size": 50
    },
    "offshore-pump": {
        "type": "item_dict",
        "name": "offshore-pump",
        "icon": "__base__/graphics/icons/offshore-pump.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "extraction-machine",
        "order": "b[fluids]-a[offshore-pump]",
        "place_result": "offshore-pump",
        "stack_size": 20
    },
    "pipe": {
        "type": "item_dict",
        "name": "pipe",
        "icon": "__base__/graphics/icons/pipe.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy-pipe-distribution",
        "order": "a[pipe]-a[pipe]",
        "place_result": "pipe",
        "stack_size": 100
    },
    "boiler": {
        "type": "item_dict",
        "name": "boiler",
        "icon": "__base__/graphics/icons/boiler.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy",
        "order": "b[steam-power]-a[boiler]",
        "place_result": "boiler",
        "stack_size": 50
    },
    "steam-engine": {
        "type": "item_dict",
        "name": "steam-engine",
        "icon": "__base__/graphics/icons/steam-engine.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy",
        "order": "b[steam-power]-b[steam-engine]",
        "place_result": "steam-engine",
        "stack_size": 10
    },
    "small-electric-pole": {
        "type": "item_dict",
        "name": "small-electric-pole",
        "icon": "__base__/graphics/icons/small-electric-pole.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy-pipe-distribution",
        "order": "a[energy]-a[small-electric-pole]",
        "place_result": "small-electric-pole",
        "stack_size": 50
    },
    "radar": {
        "type": "item_dict",
        "name": "radar",
        "icon": "__base__/graphics/icons/radar.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "defensive-structure",
        "order": "d[radar]-a[radar]",
        "place_result": "radar",
        "stack_size": 50
    },
    "small-lamp": {
        "type": "item_dict",
        "name": "small-lamp",
        "icon": "__base__/graphics/icons/small-lamp.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "circuit-network",
        "order": "a[light]-a[small-lamp]",
        "place_result": "small-lamp",
        "stack_size": 50
    },
    "pipe-to-ground": {
        "type": "item_dict",
        "name": "pipe-to-ground",
        "icon": "__base__/graphics/icons/pipe-to-ground.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy-pipe-distribution",
        "order": "a[pipe]-b[pipe-to-ground]",
        "place_result": "pipe-to-ground",
        "stack_size": 50
    },
    "assembling-machine-1": {
        "type": "item_dict",
        "name": "assembling-machine-1",
        "icon": "__base__/graphics/icons/assembling-machine-1.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "production-machine",
        "order": "a[assembling-machine-1]",
        "place_result": "assembling-machine-1",
        "stack_size": 50
    },
    "assembling-machine-2": {
        "type": "item_dict",
        "name": "assembling-machine-2",
        "icon": "__base__/graphics/icons/assembling-machine-2.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "production-machine",
        "order": "b[assembling-machine-2]",
        "place_result": "assembling-machine-2",
        "stack_size": 50
    },
    "red-wire": {
        "type": "item_dict",
        "name": "red-wire",
        "icon": "__base__/graphics/icons/red-wire.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "circuit-network",
        "order": "b[wires]-a[red-wire]",
        "stack_size": 200,
        "wire_count": 1
    },
    "green-wire": {
        "type": "item_dict",
        "name": "green-wire",
        "icon": "__base__/graphics/icons/green-wire.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "circuit-network",
        "order": "b[wires]-b[green-wire]",
        "stack_size": 200,
        "wire_count": 1
    },
    "raw-fish": {
        "type": "capsule",
        "name": "raw-fish",
        "icon": "__base__/graphics/icons/fish.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "raw-resource",
        "capsule_action": {
            "type": "use-on-self",
            "attack_parameters": {
                "type": "projectile",
                "activation_type": "consume",
                "ammo_category": "capsule",
                "cooldown": 30,
                "range": 0,
                "ammo_type": {
                    "category": "capsule",
                    "target_type": "position",
                    "action": {
                        "type": "direct",
                        "action_delivery": {
                            "type": "instant",
                            "target_effects": [
                                {
                                    "type": "damage",
                                    "damage": {
                                        "type": "physical",
                                        "amount": -80
                                    }
                                },
                                {
                                    "type": "play-sound",
                                    "sound": "sounds",
                                    "2": ".eat_fish"
                                }
                            ]
                        }
                    }
                }
            }
        },
        "order": "h[raw-fish]",
        "stack_size": 100
    },
    "repair-pack": {
        "type": "repair-tool",
        "name": "repair-pack",
        "icon": "__base__/graphics/icons/repair-pack.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "tool",
        "order": "b[repair]-a[repair-pack]",
        "speed": 2,
        "durability": 300,
        "stack_size": 100
    },
    "stone-wall": {
        "type": "item_dict",
        "name": "stone-wall",
        "icon": "__base__/graphics/icons/wall.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "defensive-structure",
        "order": "a[stone-wall]-a[stone-wall]",
        "place_result": "stone-wall",
        "stack_size": 100
    },
    "lab": {
        "type": "item_dict",
        "name": "lab",
        "icon": "__base__/graphics/icons/lab.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "production-machine",
        "order": "g[lab]",
        "place_result": "lab",
        "stack_size": 10
    },
    "copy-paste-tool": {
        "type": "copy-paste-tool",
        "name": "copy-paste-tool",
        "icon": "__base__/graphics/icons/copy-paste-tool.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "only-in-cursor",
            "hidden",
            "not-stackable"
        ],
        "subgroup": "tool",
        "order": "c[automated-construction]-x",
        "stack_size": 1,
        "draw_label_for_cursor_render": True,
        "selection_color": [
            1,
            1,
            1
        ],
        "alt_selection_color": [
            0,
            1,
            1
        ],
        "selection_mode": [
            "blueprint"
        ],
        "alt_selection_mode": [
            "blueprint"
        ],
        "selection_cursor_box_type": "copy",
        "alt_selection_cursor_box_type": "copy"
    },
    "cut-paste-tool": {
        "type": "copy-paste-tool",
        "name": "cut-paste-tool",
        "icon": "__base__/graphics/icons/cut-paste-tool.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "only-in-cursor",
            "hidden",
            "not-stackable"
        ],
        "subgroup": "tool",
        "order": "c[automated-construction]-x",
        "stack_size": 1,
        "draw_label_for_cursor_render": True,
        "selection_color": [
            1,
            1,
            1
        ],
        "alt_selection_color": [
            1,
            1,
            1
        ],
        "selection_mode": [
            "deconstruct"
        ],
        "alt_selection_mode": [
            "deconstruct"
        ],
        "selection_cursor_box_type": "copy",
        "alt_selection_cursor_box_type": "copy",
        "cuts": True
    },
    "blueprint": {
        "type": "blueprint",
        "name": "blueprint",
        "icon": "__base__/graphics/icons/blueprint.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "not-stackable",
            "spawnable"
        ],
        "subgroup": "tool",
        "order": "c[automated-construction]-a[blueprint]",
        "stack_size": 1,
        "draw_label_for_cursor_render": True,
        "selection_color": [
            57,
            156,
            251
        ],
        "alt_selection_color": [
            0.3,
            0.8,
            1
        ],
        "selection_count_button_color": [
            43,
            113,
            180
        ],
        "alt_selection_count_button_color": [
            0.3,
            0.8,
            1
        ],
        "selection_mode": [
            "blueprint"
        ],
        "alt_selection_mode": [
            "blueprint"
        ],
        "selection_cursor_box_type": "copy",
        "alt_selection_cursor_box_type": "copy",
        "open_sound": {
            "filename": "__base__/sound/item_dict-open.ogg",
            "volume": 1
        },
        "close_sound": {
            "filename": "__base__/sound/item_dict-close.ogg",
            "volume": 1
        }
    },
    "automation-science-pack": {
        "type": "tool",
        "name": "automation-science-pack",
        "localised_description": [
            "item_dict-description.science-pack"
        ],
        "icon": "__base__/graphics/icons/automation-science-pack.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "science-pack",
        "order": "a[automation-science-pack]",
        "stack_size": 200,
        "durability": 1,
        "durability_description_key": "description.science-pack-remaining-amount-key",
        "durability_description_value": "description.science-pack-remaining-amount-value"
    },
    "logistic-science-pack": {
        "type": "tool",
        "name": "logistic-science-pack",
        "localised_description": [
            "item_dict-description.science-pack"
        ],
        "icon": "__base__/graphics/icons/logistic-science-pack.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "science-pack",
        "order": "b[logistic-science-pack]",
        "stack_size": 200,
        "durability": 1,
        "durability_description_key": "description.science-pack-remaining-amount-key",
        "durability_description_value": "description.science-pack-remaining-amount-value"
    },
    "steel-plate": {
        "type": "item_dict",
        "name": "steel-plate",
        "icon": "__base__/graphics/icons/steel-plate.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "raw-material",
        "order": "d[steel-plate]",
        "stack_size": 100
    },
    "car": {
        "type": "item_dict-with-entity-data",
        "name": "car",
        "icon": "__base__/graphics/icons/car.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "transport",
        "order": "b[personal-transport]-a[car]",
        "place_result": "car",
        "stack_size": 1
    },
    "engine-unit": {
        "type": "item_dict",
        "name": "engine-unit",
        "icon": "__base__/graphics/icons/engine-unit.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "h[engine-unit]",
        "stack_size": 50
    },
    "electric-furnace": {
        "type": "item_dict",
        "name": "electric-furnace",
        "icon": "__base__/graphics/icons/electric-furnace.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "smelting-machine",
        "order": "c[electric-furnace]",
        "place_result": "electric-furnace",
        "stack_size": 50
    },
    "solid-fuel": {
        "type": "item_dict",
        "name": "solid-fuel",
        "icon": "__base__/graphics/icons/solid-fuel.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "fuel_category": "chemical",
        "fuel_value": "12MJ",
        "fuel_acceleration_multiplier": 1.2,
        "fuel_top_speed_multiplier": 1.05,
        "subgroup": "raw-material",
        "order": "c[solid-fuel]",
        "stack_size": 50
    },
    "rocket-fuel": {
        "type": "item_dict",
        "name": "rocket-fuel",
        "icon": "__base__/graphics/icons/rocket-fuel.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "fuel_category": "chemical",
        "fuel_value": "100MJ",
        "fuel_acceleration_multiplier": 1.8,
        "fuel_top_speed_multiplier": 1.15,
        "subgroup": "intermediate-product",
        "order": "p[rocket-fuel]",
        "stack_size": 10
    },
    "iron-chest": {
        "type": "item_dict",
        "name": "iron-chest",
        "icon": "__base__/graphics/icons/iron-chest.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "storage",
        "order": "a[items]-b[iron-chest]",
        "place_result": "iron-chest",
        "stack_size": 50
    },
    "big-electric-pole": {
        "type": "item_dict",
        "name": "big-electric-pole",
        "icon": "__base__/graphics/icons/big-electric-pole.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy-pipe-distribution",
        "order": "a[energy]-c[big-electric-pole]",
        "place_result": "big-electric-pole",
        "stack_size": 50
    },
    "medium-electric-pole": {
        "type": "item_dict",
        "name": "medium-electric-pole",
        "icon": "__base__/graphics/icons/medium-electric-pole.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy-pipe-distribution",
        "order": "a[energy]-b[medium-electric-pole]",
        "place_result": "medium-electric-pole",
        "stack_size": 50
    },
    "grenade": {
        "type": "capsule",
        "name": "grenade",
        "icon": "__base__/graphics/icons/grenade.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "capsule_action": {
            "type": "throw",
            "attack_parameters": {
                "type": "projectile",
                "activation_type": "throw",
                "ammo_category": "grenade",
                "cooldown": 30,
                "projectile_creation_distance": 0.6,
                "range": 15,
                "ammo_type": {
                    "category": "grenade",
                    "target_type": "position",
                    "action": [
                        {
                            "type": "direct",
                            "action_delivery": {
                                "type": "projectile",
                                "projectile": "grenade",
                                "starting_speed": 0.3
                            }
                        },
                        {
                            "type": "direct",
                            "action_delivery": {
                                "type": "instant",
                                "target_effects": [
                                    {
                                        "type": "play-sound",
                                        "sound": "sounds",
                                        "2": ".throw_projectile"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        },
        "subgroup": "capsule",
        "order": "a[grenade]-a[normal]",
        "stack_size": 100
    },
    "steel-furnace": {
        "type": "item_dict",
        "name": "steel-furnace",
        "icon": "__base__/graphics/icons/steel-furnace.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "smelting-machine",
        "order": "b[steel-furnace]",
        "place_result": "steel-furnace",
        "stack_size": 50
    },
    "gate": {
        "type": "item_dict",
        "name": "gate",
        "icon": "__base__/graphics/icons/gate.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "defensive-structure",
        "order": "a[wall]-b[gate]",
        "place_result": "gate",
        "stack_size": 50
    },
    "steel-chest": {
        "type": "item_dict",
        "name": "steel-chest",
        "icon": "__base__/graphics/icons/steel-chest.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "storage",
        "order": "a[items]-c[steel-chest]",
        "place_result": "steel-chest",
        "stack_size": 50
    },
    "solar-panel": {
        "type": "item_dict",
        "name": "solar-panel",
        "icon": "__base__/graphics/icons/solar-panel.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy",
        "order": "d[solar-panel]-a[solar-panel]",
        "place_result": "solar-panel",
        "stack_size": 50
    },
    "locomotive": {
        "type": "item_dict-with-entity-data",
        "name": "locomotive",
        "icon": "__base__/graphics/icons/locomotive.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "train-transport",
        "order": "a[train-system]-f[locomotive]",
        "place_result": "locomotive",
        "stack_size": 5
    },
    "cargo-wagon": {
        "type": "item_dict-with-entity-data",
        "name": "cargo-wagon",
        "icon": "__base__/graphics/icons/cargo-wagon.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "train-transport",
        "order": "a[train-system]-g[cargo-wagon]",
        "place_result": "cargo-wagon",
        "stack_size": 5
    },
    "rail": {
        "type": "rail-planner",
        "name": "rail",
        "icon": "__base__/graphics/icons/rail.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "localised_name": [
            "item_dict-name.rail"
        ],
        "subgroup": "train-transport",
        "order": "a[train-system]-a[rail]",
        "place_result": "straight-rail",
        "stack_size": 100,
        "straight_rail": "straight-rail",
        "curved_rail": "curved-rail"
    },
    "train-stop": {
        "type": "item_dict",
        "name": "train-stop",
        "icon": "__base__/graphics/icons/train-stop.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "train-transport",
        "order": "a[train-system]-c[train-stop]",
        "place_result": "train-stop",
        "stack_size": 10
    },
    "rail-signal": {
        "type": "item_dict",
        "name": "rail-signal",
        "icon": "__base__/graphics/icons/rail-signal.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "train-transport",
        "order": "a[train-system]-d[rail-signal]",
        "place_result": "rail-signal",
        "stack_size": 50
    },
    "rail-chain-signal": {
        "type": "item_dict",
        "name": "rail-chain-signal",
        "icon": "__base__/graphics/icons/rail-chain-signal.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "train-transport",
        "order": "a[train-system]-e[rail-signal-chain]",
        "place_result": "rail-chain-signal",
        "stack_size": 50
    },
    "concrete": {
        "type": "item_dict",
        "name": "concrete",
        "icon": "__base__/graphics/icons/concrete.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "terrain",
        "order": "b[concrete]-a[plain]",
        "stack_size": 100,
        "place_as_tile": {
            "result": "concrete",
            "condition_size": 1,
            "condition": [
                "water-tile"
            ]
        }
    },
    "refined-concrete": {
        "type": "item_dict",
        "name": "refined-concrete",
        "icon": "__base__/graphics/icons/refined-concrete.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "terrain",
        "order": "b[concrete]-c[refined]",
        "stack_size": 100,
        "place_as_tile": {
            "result": "refined-concrete",
            "condition_size": 1,
            "condition": [
                "water-tile"
            ]
        }
    },
    "hazard-concrete": {
        "type": "item_dict",
        "name": "hazard-concrete",
        "icon": "__base__/graphics/icons/hazard-concrete.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "terrain",
        "order": "b[concrete]-b[hazard]",
        "stack_size": 100,
        "place_as_tile": {
            "result": "hazard-concrete-left",
            "condition_size": 1,
            "condition": [
                "water-tile"
            ]
        }
    },
    "refined-hazard-concrete": {
        "type": "item_dict",
        "name": "refined-hazard-concrete",
        "icon": "__base__/graphics/icons/refined-hazard-concrete.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "terrain",
        "order": "b[concrete]-d[refined-hazard]",
        "stack_size": 100,
        "place_as_tile": {
            "result": "refined-hazard-concrete-left",
            "condition_size": 1,
            "condition": [
                "water-tile"
            ]
        }
    },
    "landfill": {
        "type": "item_dict",
        "name": "landfill",
        "icon": "__base__/graphics/icons/landfill.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "terrain",
        "order": "c[landfill]-a[dirt]",
        "stack_size": 100,
        "place_as_tile": {
            "result": "landfill",
            "condition_size": 1,
            "condition": [
                "ground-tile"
            ]
        }
    },
    "accumulator": {
        "type": "item_dict",
        "name": "accumulator",
        "icon": "__base__/graphics/icons/accumulator.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy",
        "order": "e[accumulator]-a[accumulator]",
        "place_result": "accumulator",
        "stack_size": 50
    },
    "transport-belt": {
        "type": "item_dict",
        "name": "transport-belt",
        "icon": "__base__/graphics/icons/transport-belt.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "belt",
        "order": "a[transport-belt]-a[transport-belt]",
        "place_result": "transport-belt",
        "stack_size": 100
    },
    "fast-transport-belt": {
        "type": "item_dict",
        "name": "fast-transport-belt",
        "icon": "__base__/graphics/icons/fast-transport-belt.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "belt",
        "order": "a[transport-belt]-b[fast-transport-belt]",
        "place_result": "fast-transport-belt",
        "stack_size": 100
    },
    "express-transport-belt": {
        "type": "item_dict",
        "name": "express-transport-belt",
        "icon": "__base__/graphics/icons/express-transport-belt.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "belt",
        "order": "a[transport-belt]-c[express-transport-belt]",
        "place_result": "express-transport-belt",
        "stack_size": 100
    },
    "stack-inserter": {
        "type": "item_dict",
        "name": "stack-inserter",
        "icon": "__base__/graphics/icons/stack-inserter.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "inserter",
        "order": "f[stack-inserter]",
        "place_result": "stack-inserter",
        "stack_size": 50
    },
    "stack-filter-inserter": {
        "type": "item_dict",
        "name": "stack-filter-inserter",
        "icon": "__base__/graphics/icons/stack-filter-inserter.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "inserter",
        "order": "g[stack-filter-inserter]",
        "place_result": "stack-filter-inserter",
        "stack_size": 50
    },
    "assembling-machine-3": {
        "type": "item_dict",
        "name": "assembling-machine-3",
        "icon": "__base__/graphics/icons/assembling-machine-3.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "production-machine",
        "order": "c[assembling-machine-3]",
        "place_result": "assembling-machine-3",
        "stack_size": 50
    },
    "fluid-wagon": {
        "type": "item_dict-with-entity-data",
        "name": "fluid-wagon",
        "icon": "__base__/graphics/icons/fluid-wagon.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "train-transport",
        "order": "a[train-system]-h[fluid-wagon]",
        "place_result": "fluid-wagon",
        "stack_size": 5
    },
    "artillery-wagon": {
        "type": "item_dict-with-entity-data",
        "name": "artillery-wagon",
        "icon": "__base__/graphics/icons/artillery-wagon.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "train-transport",
        "order": "a[train-system]-i[artillery-wagon]",
        "place_result": "artillery-wagon",
        "stack_size": 5
    },
    "player-port": {
        "type": "item_dict",
        "name": "player-port",
        "icon": "__base__/graphics/icons/player-port.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "defensive-structure",
        "order": "z[not-used]",
        "place_result": "player-port",
        "stack_size": 50
    },
    "tank": {
        "type": "item_dict-with-entity-data",
        "name": "tank",
        "icon": "__base__/graphics/icons/tank.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "transport",
        "order": "b[personal-transport]-b[tank]",
        "place_result": "tank",
        "stack_size": 1
    },
    "chemical-science-pack": {
        "type": "tool",
        "name": "chemical-science-pack",
        "localised_description": [
            "item_dict-description.science-pack"
        ],
        "icon": "__base__/graphics/icons/chemical-science-pack.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "science-pack",
        "order": "d[chemical-science-pack]",
        "stack_size": 200,
        "durability": 1,
        "durability_description_key": "description.science-pack-remaining-amount-key",
        "durability_description_value": "description.science-pack-remaining-amount-value"
    },
    "military-science-pack": {
        "type": "tool",
        "name": "military-science-pack",
        "localised_description": [
            "item_dict-description.science-pack"
        ],
        "icon": "__base__/graphics/icons/military-science-pack.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "science-pack",
        "order": "c[military-science-pack]",
        "stack_size": 200,
        "durability": 1,
        "durability_description_key": "description.science-pack-remaining-amount-key",
        "durability_description_value": "description.science-pack-remaining-amount-value"
    },
    "production-science-pack": {
        "type": "tool",
        "name": "production-science-pack",
        "localised_description": [
            "item_dict-description.science-pack"
        ],
        "icon": "__base__/graphics/icons/production-science-pack.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "science-pack",
        "order": "e[production-science-pack]",
        "stack_size": 200,
        "durability": 1,
        "durability_description_key": "description.science-pack-remaining-amount-key",
        "durability_description_value": "description.science-pack-remaining-amount-value"
    },
    "utility-science-pack": {
        "type": "tool",
        "name": "utility-science-pack",
        "localised_description": [
            "item_dict-description.science-pack"
        ],
        "icon": "__base__/graphics/icons/utility-science-pack.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "science-pack",
        "order": "f[utility-science-pack]",
        "stack_size": 200,
        "durability": 1,
        "durability_description_key": "description.science-pack-remaining-amount-key",
        "durability_description_value": "description.science-pack-remaining-amount-value"
    },
    "space-science-pack": {
        "type": "tool",
        "name": "space-science-pack",
        "icon": "__base__/graphics/icons/space-science-pack.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "science-pack",
        "order": "g[space-science-pack]",
        "stack_size": 2000,
        "durability": 1,
        "rocket_launch_product": [
            "raw-fish",
            1
        ],
        "durability_description_key": "description.science-pack-remaining-amount-key",
        "durability_description_value": "description.science-pack-remaining-amount-value"
    },
    "underground-belt": {
        "type": "item_dict",
        "name": "underground-belt",
        "icon": "__base__/graphics/icons/underground-belt.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "belt",
        "order": "b[underground-belt]-a[underground-belt]",
        "place_result": "underground-belt",
        "stack_size": 50
    },
    "fast-underground-belt": {
        "type": "item_dict",
        "name": "fast-underground-belt",
        "icon": "__base__/graphics/icons/fast-underground-belt.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "belt",
        "order": "b[underground-belt]-b[fast-underground-belt]",
        "place_result": "fast-underground-belt",
        "stack_size": 50
    },
    "express-underground-belt": {
        "type": "item_dict",
        "name": "express-underground-belt",
        "icon": "__base__/graphics/icons/express-underground-belt.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "belt",
        "order": "b[underground-belt]-c[express-underground-belt]",
        "place_result": "express-underground-belt",
        "stack_size": 50
    },
    "splitter": {
        "type": "item_dict",
        "name": "splitter",
        "icon": "__base__/graphics/icons/splitter.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "belt",
        "order": "c[splitter]-a[splitter]",
        "place_result": "splitter",
        "stack_size": 50
    },
    "fast-splitter": {
        "type": "item_dict",
        "name": "fast-splitter",
        "icon": "__base__/graphics/icons/fast-splitter.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "belt",
        "order": "c[splitter]-b[fast-splitter]",
        "place_result": "fast-splitter",
        "stack_size": 50
    },
    "express-splitter": {
        "type": "item_dict",
        "name": "express-splitter",
        "icon": "__base__/graphics/icons/express-splitter.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "belt",
        "order": "c[splitter]-c[express-splitter]",
        "place_result": "express-splitter",
        "stack_size": 50
    },
    "loader": {
        "type": "item_dict",
        "name": "loader",
        "icon": "__base__/graphics/icons/loader.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "belt",
        "order": "d[loader]-a[basic-loader]",
        "place_result": "loader",
        "stack_size": 50
    },
    "fast-loader": {
        "type": "item_dict",
        "name": "fast-loader",
        "icon": "__base__/graphics/icons/fast-loader.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "belt",
        "order": "d[loader]-b[fast-loader]",
        "place_result": "fast-loader",
        "stack_size": 50
    },
    "express-loader": {
        "type": "item_dict",
        "name": "express-loader",
        "icon": "__base__/graphics/icons/express-loader.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "belt",
        "order": "d[loader]-c[express-loader]",
        "place_result": "express-loader",
        "stack_size": 50
    },
    "advanced-circuit": {
        "type": "item_dict",
        "name": "advanced-circuit",
        "icon": "__base__/graphics/icons/advanced-circuit.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "f[advanced-circuit]",
        "stack_size": 200
    },
    "processing-unit": {
        "type": "item_dict",
        "name": "processing-unit",
        "icon": "__base__/graphics/icons/processing-unit.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "g[processing-unit]",
        "stack_size": 100
    },
    "logistic-robot": {
        "type": "item_dict",
        "name": "logistic-robot",
        "icon": "__base__/graphics/icons/logistic-robot.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "logistic-network",
        "order": "a[robot]-a[logistic-robot]",
        "place_result": "logistic-robot",
        "stack_size": 50
    },
    "construction-robot": {
        "type": "item_dict",
        "name": "construction-robot",
        "icon": "__base__/graphics/icons/construction-robot.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "logistic-network",
        "order": "a[robot]-b[construction-robot]",
        "place_result": "construction-robot",
        "stack_size": 50
    },
    "logistic-chest-passive-provider": {
        "type": "item_dict",
        "name": "logistic-chest-passive-provider",
        "icon": "__base__/graphics/icons/logistic-chest-passive-provider.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "logistic-network",
        "order": "b[storage]-c[logistic-chest-passive-provider]",
        "place_result": "logistic-chest-passive-provider",
        "stack_size": 50
    },
    "logistic-chest-active-provider": {
        "type": "item_dict",
        "name": "logistic-chest-active-provider",
        "icon": "__base__/graphics/icons/logistic-chest-active-provider.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "logistic-network",
        "order": "b[storage]-c[logistic-chest-active-provider]",
        "place_result": "logistic-chest-active-provider",
        "stack_size": 50
    },
    "logistic-chest-storage": {
        "type": "item_dict",
        "name": "logistic-chest-storage",
        "icon": "__base__/graphics/icons/logistic-chest-storage.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "logistic-network",
        "order": "b[storage]-c[logistic-chest-storage]",
        "place_result": "logistic-chest-storage",
        "stack_size": 50
    },
    "logistic-chest-buffer": {
        "type": "item_dict",
        "name": "logistic-chest-buffer",
        "icon": "__base__/graphics/icons/logistic-chest-buffer.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "logistic-network",
        "order": "b[storage]-d[logistic-chest-buffer]",
        "place_result": "logistic-chest-buffer",
        "stack_size": 50
    },
    "logistic-chest-requester": {
        "type": "item_dict",
        "name": "logistic-chest-requester",
        "icon": "__base__/graphics/icons/logistic-chest-requester.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "logistic-network",
        "order": "b[storage]-e[logistic-chest-requester]",
        "place_result": "logistic-chest-requester",
        "stack_size": 50
    },
    "rocket-silo": {
        "type": "item_dict",
        "name": "rocket-silo",
        "icon": "__base__/graphics/icons/rocket-silo.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "space-related",
        "order": "e[rocket-silo]",
        "place_result": "rocket-silo",
        "stack_size": 1
    },
    "roboport": {
        "type": "item_dict",
        "name": "roboport",
        "icon": "__base__/graphics/icons/roboport.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "logistic-network",
        "order": "c[signal]-a[roboport]",
        "place_result": "roboport",
        "stack_size": 10
    },
    "coin": {
        "type": "item_dict",
        "name": "coin",
        "icon": "__base__/graphics/icons/coin.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "science-pack",
        "order": "y",
        "stack_size": 100000
    },
    "substation": {
        "type": "item_dict",
        "name": "substation",
        "icon": "__base__/graphics/icons/substation.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy-pipe-distribution",
        "order": "a[energy]-d[substation]",
        "place_result": "substation",
        "stack_size": 50
    },
    "beacon": {
        "type": "item_dict",
        "name": "beacon",
        "icon": "__base__/graphics/icons/beacon.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "module",
        "order": "a[beacon]",
        "place_result": "beacon",
        "stack_size": 10
    },
    "storage-tank": {
        "type": "item_dict",
        "name": "storage-tank",
        "icon": "__base__/graphics/icons/storage-tank.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "storage",
        "order": "b[fluid]-a[storage-tank]",
        "place_result": "storage-tank",
        "stack_size": 50
    },
    "pump": {
        "type": "item_dict",
        "name": "pump",
        "icon": "__base__/graphics/icons/pump.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy-pipe-distribution",
        "order": "b[pipe]-c[pump]",
        "place_result": "pump",
        "stack_size": 50
    },
    "upgrade-planner": {
        "type": "upgrade-item_dict",
        "name": "upgrade-planner",
        "icon": "__base__/graphics/icons/upgrade-planner.png",
        "flags": [
            "spawnable"
        ],
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "tool",
        "order": "c[automated-construction]-c[upgrade-planner]",
        "stack_size": 1,
        "mapper_count": 24,
        "selection_color": [
            71,
            255,
            73
        ],
        "alt_selection_color": [
            239,
            153,
            34
        ],
        "reverse_selection_color": [
            246,
            255,
            0
        ],
        "selection_mode": [
            "upgrade"
        ],
        "alt_selection_mode": [
            "cancel-upgrade"
        ],
        "reverse_selection_mode": [
            "downgrade"
        ],
        "selection_cursor_box_type": "not-allowed",
        "alt_selection_cursor_box_type": "not-allowed",
        "reverse_selection_cursor_box_type": "not-allowed",
        "open_sound": {
            "filename": "__base__/sound/item_dict-open.ogg",
            "volume": 1
        },
        "close_sound": {
            "filename": "__base__/sound/item_dict-close.ogg",
            "volume": 1
        }
    },
    "deconstruction-planner": {
        "type": "deconstruction-item_dict",
        "name": "deconstruction-planner",
        "icon": "__base__/graphics/icons/deconstruction-planner.png",
        "flags": [
            "spawnable"
        ],
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "tool",
        "order": "c[automated-construction]-b[deconstruction-planner]",
        "stack_size": 1,
        "entity_filter_count": 30,
        "tile_filter_count": 30,
        "selection_color": [
            255,
            24,
            24
        ],
        "selection_count_button_color": [
            195,
            52,
            52
        ],
        "alt_selection_color": [
            239,
            153,
            34
        ],
        "alt_selection_count_button_color": [
            255,
            176,
            66
        ],
        "selection_mode": [
            "deconstruct"
        ],
        "alt_selection_mode": [
            "cancel-deconstruct"
        ],
        "selection_cursor_box_type": "not-allowed",
        "alt_selection_cursor_box_type": "not-allowed",
        "open_sound": {
            "filename": "__base__/sound/item_dict-open.ogg",
            "volume": 1
        },
        "close_sound": {
            "filename": "__base__/sound/item_dict-close.ogg",
            "volume": 1
        }
    },
    "blueprint-book": {
        "type": "blueprint-book",
        "name": "blueprint-book",
        "icon": "__base__/graphics/icons/blueprint-book.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "spawnable"
        ],
        "subgroup": "tool",
        "order": "c[automated-construction]-d[blueprint-book]",
        "stack_size": 1,
        "inventory_size": "dynamic",
        "open_sound": {
            "filename": "__base__/sound/item_dict-open.ogg",
            "volume": 1
        },
        "close_sound": {
            "filename": "__base__/sound/item_dict-close.ogg",
            "volume": 1
        }
    },
    "pumpjack": {
        "type": "item_dict",
        "name": "pumpjack",
        "icon": "__base__/graphics/icons/pumpjack.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "extraction-machine",
        "order": "b[fluids]-b[pumpjack]",
        "place_result": "pumpjack",
        "stack_size": 20
    },
    "oil-refinery": {
        "type": "item_dict",
        "name": "oil-refinery",
        "icon": "__base__/graphics/icons/oil-refinery.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "production-machine",
        "order": "d[refinery]",
        "place_result": "oil-refinery",
        "stack_size": 10
    },
    "chemical-plant": {
        "type": "item_dict",
        "name": "chemical-plant",
        "icon": "__base__/graphics/icons/chemical-plant.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "production-machine",
        "order": "e[chemical-plant]",
        "place_result": "chemical-plant",
        "stack_size": 10
    },
    "sulfur": {
        "type": "item_dict",
        "name": "sulfur",
        "icon": "__base__/graphics/icons/sulfur.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "raw-material",
        "order": "g[sulfur]",
        "stack_size": 50
    },
    "empty-barrel": {
        "type": "item_dict",
        "name": "empty-barrel",
        "icon": "__base__/graphics/icons/fluid/barreling/empty-barrel.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "d[empty-barrel]",
        "stack_size": 10
    },
    "plastic-bar": {
        "type": "item_dict",
        "name": "plastic-bar",
        "icon": "__base__/graphics/icons/plastic-bar.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "raw-material",
        "order": "f[plastic-bar]",
        "stack_size": 100
    },
    "electric-engine-unit": {
        "type": "item_dict",
        "name": "electric-engine-unit",
        "icon": "__base__/graphics/icons/electric-engine-unit.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "i[electric-engine-unit]",
        "stack_size": 50
    },
    "explosives": {
        "type": "item_dict",
        "name": "explosives",
        "icon": "__base__/graphics/icons/explosives.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "raw-material",
        "order": "j[explosives]",
        "stack_size": 50
    },
    "battery": {
        "type": "item_dict",
        "name": "battery",
        "icon": "__base__/graphics/icons/battery.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "raw-material",
        "order": "h[battery]",
        "stack_size": 200
    },
    "flying-robot-frame": {
        "type": "item_dict",
        "name": "flying-robot-frame",
        "icon": "__base__/graphics/icons/flying-robot-frame.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "l[flying-robot-frame]",
        "stack_size": 50
    },
    "low-density-structure": {
        "type": "item_dict",
        "name": "low-density-structure",
        "icon": "__base__/graphics/icons/low-density-structure.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "o[low-density-structure]",
        "stack_size": 10
    },
    "nuclear-fuel": {
        "type": "item_dict",
        "name": "nuclear-fuel",
        "icon": "__base__/graphics/icons/nuclear-fuel.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "pictures": {
            "layers": [
                {
                    "size": 64,
                    "filename": "__base__/graphics/icons/nuclear-fuel.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                },
                {
                    "draw_as_light": True,
                    "flags": [
                        "light"
                    ],
                    "size": 64,
                    "filename": "__base__/graphics/icons/nuclear-fuel-light.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                }
            ]
        },
        "fuel_category": "chemical",
        "fuel_value": "1.21GJ",
        "fuel_acceleration_multiplier": 2.5,
        "fuel_top_speed_multiplier": 1.15,
        "subgroup": "intermediate-product",
        "order": "q[uranium-rocket-fuel]",
        "stack_size": 1
    },
    "rocket-control-unit": {
        "type": "item_dict",
        "name": "rocket-control-unit",
        "icon": "__base__/graphics/icons/rocket-control-unit.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "n[rocket-control-unit]",
        "stack_size": 10
    },
    "rocket-part": {
        "type": "item_dict",
        "name": "rocket-part",
        "icon": "__base__/graphics/icons/rocket-part.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "intermediate-product",
        "order": "q[rocket-part]",
        "stack_size": 5
    },
    "satellite": {
        "type": "item_dict",
        "name": "satellite",
        "icon": "__base__/graphics/icons/satellite.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "space-related",
        "order": "m[satellite]",
        "stack_size": 1,
        "rocket_launch_product": [
            "space-science-pack",
            1000
        ]
    },
    "spidertron": {
        "type": "item_dict-with-entity-data",
        "name": "spidertron",
        "icon": "__base__/graphics/icons/spidertron.png",
        "icon_tintable": "__base__/graphics/icons/spidertron-tintable.png",
        "icon_tintable_mask": "__base__/graphics/icons/spidertron-tintable-mask.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "transport",
        "order": "b[personal-transport]-c[spidertron]-a[spider]",
        "place_result": "spidertron",
        "stack_size": 1
    },
    "spidertron-remote": {
        "type": "spidertron-remote",
        "name": "spidertron-remote",
        "icon": "__base__/graphics/icons/spidertron-remote.png",
        "icon_color_indicator_mask": "__base__/graphics/icons/spidertron-remote-mask.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "transport",
        "order": "b[personal-transport]-c[spidertron]-b[remote]",
        "stack_size": 1
    },
    "selection-tool": {
        "type": "selection-tool",
        "name": "selection-tool",
        "icon": "__base__/graphics/icons/blueprint.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden",
            "not-stackable",
            "spawnable"
        ],
        "subgroup": "other",
        "order": "e[automated-construction]-a[blueprint]",
        "stack_size": 1,
        "selection_color": {
            "r": 255,
            "g": 255,
            "b": 255
        },
        "alt_selection_color": {
            "r": 0,
            "g": 1,
            "b": 0
        },
        "selection_mode": [
            "blueprint"
        ],
        "alt_selection_mode": [
            "blueprint"
        ],
        "selection_cursor_box_type": "copy",
        "alt_selection_cursor_box_type": "copy"
    },
    "electric-energy-interface": {
        "type": "item_dict",
        "name": "electric-energy-interface",
        "icons": [
            {
                "icon": "__base__/graphics/icons/accumulator.png",
                "tint": {
                    "r": 1,
                    "g": 0.8,
                    "b": 1,
                    "a": 1
                }
            }
        ],
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "a[electric-energy-interface]-b[electric-energy-interface]",
        "place_result": "electric-energy-interface",
        "stack_size": 50
    },
    "heat-interface": {
        "type": "item_dict",
        "name": "heat-interface",
        "icon": "__base__/graphics/icons/heat-interface.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "b[heat-interface]",
        "place_result": "heat-interface",
        "stack_size": 20
    },
    "nuclear-reactor": {
        "type": "item_dict",
        "name": "nuclear-reactor",
        "icon": "__base__/graphics/icons/nuclear-reactor.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy",
        "order": "f[nuclear-energy]-a[reactor]",
        "place_result": "nuclear-reactor",
        "stack_size": 10
    },
    "uranium-235": {
        "type": "item_dict",
        "name": "uranium-235",
        "icon": "__base__/graphics/icons/uranium-235.png",
        "pictures": {
            "layers": [
                {
                    "size": 64,
                    "filename": "__base__/graphics/icons/uranium-235.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                },
                {
                    "draw_as_light": True,
                    "blend_mode": "additive",
                    "size": 64,
                    "filename": "__base__/graphics/icons/uranium-235.png",
                    "scale": 0.25,
                    "tint": {
                        "r": 0.3,
                        "g": 0.3,
                        "b": 0.3,
                        "a": 0.3
                    },
                    "mipmap_count": 4
                }
            ]
        },
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "r[uranium-235]",
        "stack_size": 100
    },
    "uranium-238": {
        "type": "item_dict",
        "name": "uranium-238",
        "icon": "__base__/graphics/icons/uranium-238.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "r[uranium-238]",
        "stack_size": 100
    },
    "centrifuge": {
        "type": "item_dict",
        "name": "centrifuge",
        "icon": "__base__/graphics/icons/centrifuge.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "production-machine",
        "order": "g[centrifuge]",
        "place_result": "centrifuge",
        "stack_size": 50
    },
    "uranium-fuel-cell": {
        "type": "item_dict",
        "name": "uranium-fuel-cell",
        "icon": "__base__/graphics/icons/uranium-fuel-cell.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "pictures": {
            "layers": [
                {
                    "size": 64,
                    "filename": "__base__/graphics/icons/uranium-fuel-cell.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                },
                {
                    "draw_as_light": True,
                    "flags": [
                        "light"
                    ],
                    "size": 64,
                    "filename": "__base__/graphics/icons/uranium-fuel-cell-light.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                }
            ]
        },
        "subgroup": "intermediate-product",
        "order": "r[uranium-processing]-a[uranium-fuel-cell]",
        "fuel_category": "nuclear",
        "burnt_result": "used-up-uranium-fuel-cell",
        "fuel_value": "8GJ",
        "stack_size": 50
    },
    "used-up-uranium-fuel-cell": {
        "type": "item_dict",
        "name": "used-up-uranium-fuel-cell",
        "icon": "__base__/graphics/icons/used-up-uranium-fuel-cell.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "intermediate-product",
        "order": "r[used-up-uranium-fuel-cell]",
        "stack_size": 50
    },
    "heat-exchanger": {
        "type": "item_dict",
        "name": "heat-exchanger",
        "icon": "__base__/graphics/icons/heat-boiler.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy",
        "order": "f[nuclear-energy]-c[heat-exchanger]",
        "place_result": "heat-exchanger",
        "stack_size": 50
    },
    "steam-turbine": {
        "type": "item_dict",
        "name": "steam-turbine",
        "icon": "__base__/graphics/icons/steam-turbine.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy",
        "order": "f[nuclear-energy]-d[steam-turbine]",
        "place_result": "steam-turbine",
        "stack_size": 10
    },
    "heat-pipe": {
        "type": "item_dict",
        "name": "heat-pipe",
        "icon": "__base__/graphics/icons/heat-pipe.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "energy",
        "order": "f[nuclear-energy]-b[heat-pipe]",
        "place_result": "heat-pipe",
        "stack_size": 50
    },
    "simple-entity-with-force": {
        "type": "item_dict",
        "name": "simple-entity-with-force",
        "icon": "__base__/graphics/icons/steel-chest.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "s[simple-entity-with-force]-f[simple-entity-with-force]",
        "place_result": "simple-entity-with-force",
        "stack_size": 50
    },
    "simple-entity-with-owner": {
        "type": "item_dict",
        "name": "simple-entity-with-owner",
        "icon": "__base__/graphics/icons/wooden-chest.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "s[simple-entity-with-owner]-o[simple-entity-with-owner]",
        "place_result": "simple-entity-with-owner",
        "stack_size": 50
    },
    "item_dict-with-tags": {
        "type": "item_dict-with-tags",
        "name": "item_dict-with-tags",
        "icon": "__base__/graphics/icons/wooden-chest.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "s[item_dict-with-tags]-o[item_dict-with-tags]",
        "stack_size": 1
    },
    "item_dict-with-label": {
        "type": "item_dict-with-label",
        "name": "item_dict-with-label",
        "icon": "__base__/graphics/icons/wooden-chest.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "s[item_dict-with-label]-o[item_dict-with-label]",
        "stack_size": 1
    },
    "item_dict-with-inventory": {
        "type": "item_dict-with-inventory",
        "name": "item_dict-with-inventory",
        "icon": "__base__/graphics/icons/wooden-chest.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "s[item_dict-with-inventory]-o[item_dict-with-inventory]",
        "stack_size": 1,
        "inventory_size": 1
    },
    "infinity-chest": {
        "type": "item_dict",
        "name": "infinity-chest",
        "icon": "__base__/graphics/icons/infinity-chest.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "c[item_dict]-o[infinity-chest]",
        "stack_size": 10,
        "place_result": "infinity-chest"
    },
    "infinity-pipe": {
        "type": "item_dict",
        "name": "infinity-pipe",
        "icons": [
            {
                "icon": "__base__/graphics/icons/pipe.png",
                "tint": {
                    "r": 0.5,
                    "g": 0.5,
                    "b": 1
                }
            }
        ],
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "d[item_dict]-o[infinity-pipe]",
        "stack_size": 10,
        "place_result": "infinity-pipe"
    },
    "burner-generator": {
        "type": "item_dict",
        "name": "burner-generator",
        "icon": "__base__/graphics/icons/steam-engine.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "t[item_dict]-o[burner-generator]",
        "stack_size": 10,
        "place_result": "burner-generator"
    },
    "linked-chest": {
        "type": "item_dict",
        "name": "linked-chest",
        "icon": "__base__/graphics/icons/linked-chest-icon.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "a[items]-a[linked-chest]",
        "place_result": "linked-chest",
        "stack_size": 10
    },
    "linked-belt": {
        "type": "item_dict",
        "name": "linked-belt",
        "icon": "__base__/graphics/icons/linked-belt.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "other",
        "order": "b[items]-b[linked-belt]",
        "place_result": "linked-belt",
        "stack_size": 10
    },
    "speed-module": {
        "type": "module",
        "name": "speed-module",
        "localised_description": [
            "item_dict-description.speed-module"
        ],
        "icon": "__base__/graphics/icons/speed-module.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "module",
        "category": "speed",
        "tier": 1,
        "order": "a[speed]-a[speed-module-1]",
        "stack_size": 50,
        "effect": {
            "speed": {
                "bonus": 0.2
            },
            "consumption": {
                "bonus": 0.5
            }
        },
        "beacon_tint": {
            "primary": {
                "r": 0.441,
                "g": 0.714,
                "b": 1.0,
                "a": 1.0
            },
            "secondary": {
                "r": 0.388,
                "g": 0.976,
                "b": 1.0,
                "a": 1.0
            }
        },
        "art_style": "vanilla",
        "requires_beacon_alt_mode": False
    },
    "speed-module-2": {
        "type": "module",
        "name": "speed-module-2",
        "localised_description": [
            "item_dict-description.speed-module"
        ],
        "icon": "__base__/graphics/icons/speed-module-2.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "module",
        "category": "speed",
        "tier": 2,
        "order": "a[speed]-b[speed-module-2]",
        "stack_size": 50,
        "effect": {
            "speed": {
                "bonus": 0.3
            },
            "consumption": {
                "bonus": 0.6
            }
        },
        "beacon_tint": {
            "primary": {
                "r": 0.441,
                "g": 0.714,
                "b": 1.0,
                "a": 1.0
            },
            "secondary": {
                "r": 0.388,
                "g": 0.976,
                "b": 1.0,
                "a": 1.0
            }
        },
        "art_style": "vanilla",
        "requires_beacon_alt_mode": False
    },
    "speed-module-3": {
        "type": "module",
        "name": "speed-module-3",
        "localised_description": [
            "item_dict-description.speed-module"
        ],
        "icon": "__base__/graphics/icons/speed-module-3.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "module",
        "category": "speed",
        "tier": 3,
        "order": "a[speed]-c[speed-module-3]",
        "stack_size": 50,
        "effect": {
            "speed": {
                "bonus": 0.5
            },
            "consumption": {
                "bonus": 0.7
            }
        },
        "beacon_tint": {
            "primary": {
                "r": 0.441,
                "g": 0.714,
                "b": 1.0,
                "a": 1.0
            },
            "secondary": {
                "r": 0.388,
                "g": 0.976,
                "b": 1.0,
                "a": 1.0
            }
        },
        "art_style": "vanilla",
        "requires_beacon_alt_mode": False
    },
    "effectivity-module": {
        "type": "module",
        "name": "effectivity-module",
        "localised_description": [
            "item_dict-description.effectivity-module"
        ],
        "icon": "__base__/graphics/icons/effectivity-module.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "module",
        "category": "effectivity",
        "tier": 1,
        "order": "c[effectivity]-a[effectivity-module-1]",
        "stack_size": 50,
        "effect": {
            "consumption": {
                "bonus": -0.3
            }
        },
        "beacon_tint": {
            "primary": [
                0,
                1,
                0
            ],
            "secondary": {
                "r": 0.37,
                "g": 1.0,
                "b": 0.37,
                "a": 1.0
            }
        },
        "art_style": "vanilla",
        "requires_beacon_alt_mode": False
    },
    "effectivity-module-2": {
        "type": "module",
        "name": "effectivity-module-2",
        "localised_description": [
            "item_dict-description.effectivity-module"
        ],
        "icon": "__base__/graphics/icons/effectivity-module-2.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "module",
        "category": "effectivity",
        "tier": 2,
        "order": "c[effectivity]-b[effectivity-module-2]",
        "stack_size": 50,
        "effect": {
            "consumption": {
                "bonus": -0.4
            }
        },
        "beacon_tint": {
            "primary": [
                0,
                1,
                0
            ],
            "secondary": {
                "r": 0.37,
                "g": 1.0,
                "b": 0.37,
                "a": 1.0
            }
        },
        "art_style": "vanilla",
        "requires_beacon_alt_mode": False
    },
    "effectivity-module-3": {
        "type": "module",
        "name": "effectivity-module-3",
        "localised_description": [
            "item_dict-description.effectivity-module"
        ],
        "icon": "__base__/graphics/icons/effectivity-module-3.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "module",
        "category": "effectivity",
        "tier": 3,
        "order": "c[effectivity]-c[effectivity-module-3]",
        "stack_size": 50,
        "effect": {
            "consumption": {
                "bonus": -0.5
            }
        },
        "beacon_tint": {
            "primary": [
                0,
                1,
                0
            ],
            "secondary": {
                "r": 0.37,
                "g": 1.0,
                "b": 0.37,
                "a": 1.0
            }
        },
        "art_style": "vanilla",
        "requires_beacon_alt_mode": False
    },
    "productivity-module": {
        "type": "module",
        "name": "productivity-module",
        "localised_description": [
            "item_dict-description.productivity-module"
        ],
        "icon": "__base__/graphics/icons/productivity-module.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "module",
        "category": "productivity",
        "tier": 1,
        "order": "c[productivity]-a[productivity-module-1]",
        "stack_size": 50,
        "effect": {
            "productivity": {
                "bonus": 0.04
            },
            "consumption": {
                "bonus": 0.4
            },
            "pollution": {
                "bonus": 0.05
            },
            "speed": {
                "bonus": -0.05
            }
        },
        "limitation": "productivity_module_limitation",
        "13": ")",
        "limitation_message_key": "production-module-usable-only-on-intermediates"
    },
    "productivity-module-2": {
        "type": "module",
        "name": "productivity-module-2",
        "localised_description": [
            "item_dict-description.productivity-module"
        ],
        "icon": "__base__/graphics/icons/productivity-module-2.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "module",
        "category": "productivity",
        "tier": 2,
        "order": "c[productivity]-b[productivity-module-2]",
        "stack_size": 50,
        "effect": {
            "productivity": {
                "bonus": 0.06
            },
            "consumption": {
                "bonus": 0.6
            },
            "pollution": {
                "bonus": 0.07
            },
            "speed": {
                "bonus": -0.1
            }
        },
        "limitation": "productivity_module_limitation",
        "13": ")",
        "limitation_message_key": "production-module-usable-only-on-intermediates"
    },
    "productivity-module-3": {
        "type": "module",
        "name": "productivity-module-3",
        "localised_description": [
            "item_dict-description.productivity-module"
        ],
        "icon": "__base__/graphics/icons/productivity-module-3.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "module",
        "category": "productivity",
        "tier": 3,
        "order": "c[productivity]-c[productivity-module-3]",
        "stack_size": 50,
        "effect": {
            "productivity": {
                "bonus": 0.1
            },
            "consumption": {
                "bonus": 0.8
            },
            "pollution": {
                "bonus": 0.1
            },
            "speed": {
                "bonus": -0.15
            }
        },
        "limitation": "productivity_module_limitation",
        "13": ")",
        "limitation_message_key": "production-module-usable-only-on-intermediates"
    },
    "flamethrower-ammo": {
        "type": "ammo",
        "name": "flamethrower-ammo",
        "icon": "__base__/graphics/icons/flamethrower-ammo.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "ammo_type": [
            {
                "source_type": "default",
                "category": "flamethrower",
                "target_type": "position",
                "clamp_position": True,
                "action": {
                    "type": "direct",
                    "action_delivery": {
                        "type": "stream",
                        "stream": "handheld-flamethrower-fire-stream"
                    }
                }
            },
            {
                "source_type": "vehicle",
                "consumption_modifier": 1.125,
                "category": "flamethrower",
                "target_type": "position",
                "clamp_position": True,
                "action": {
                    "type": "direct",
                    "action_delivery": {
                        "type": "stream",
                        "stream": "tank-flamethrower-fire-stream"
                    }
                }
            }
        ],
        "magazine_size": 100,
        "subgroup": "ammo",
        "order": "e[flamethrower]",
        "stack_size": 100
    },
    "rocket": {
        "type": "ammo",
        "name": "rocket",
        "icon": "__base__/graphics/icons/rocket.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "ammo_type": {
            "category": "rocket",
            "action": {
                "type": "direct",
                "action_delivery": {
                    "type": "projectile",
                    "projectile": "rocket",
                    "starting_speed": 0.1,
                    "source_effects": {
                        "type": "create-entity",
                        "entity_name": "explosion-hit"
                    }
                }
            }
        },
        "subgroup": "ammo",
        "order": "d[rocket-launcher]-a[basic]",
        "stack_size": 200
    },
    "explosive-rocket": {
        "type": "ammo",
        "name": "explosive-rocket",
        "icon": "__base__/graphics/icons/explosive-rocket.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "ammo_type": {
            "category": "rocket",
            "action": {
                "type": "direct",
                "action_delivery": {
                    "type": "projectile",
                    "projectile": "explosive-rocket",
                    "starting_speed": 0.1,
                    "source_effects": {
                        "type": "create-entity",
                        "entity_name": "explosion-hit"
                    }
                }
            }
        },
        "subgroup": "ammo",
        "order": "d[rocket-launcher]-b[explosive]",
        "stack_size": 200
    },
    "atomic-bomb": {
        "type": "ammo",
        "name": "atomic-bomb",
        "icon": "__base__/graphics/icons/atomic-bomb.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "pictures": {
            "layers": [
                {
                    "size": 64,
                    "filename": "__base__/graphics/icons/atomic-bomb.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                },
                {
                    "draw_as_light": True,
                    "flags": [
                        "light"
                    ],
                    "size": 64,
                    "filename": "__base__/graphics/icons/atomic-bomb-light.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                }
            ]
        },
        "ammo_type": {
            "range_modifier": 1.5,
            "cooldown_modifier": 10,
            "target_type": "position",
            "category": "rocket",
            "action": {
                "type": "direct",
                "action_delivery": {
                    "type": "projectile",
                    "projectile": "atomic-rocket",
                    "starting_speed": 0.05,
                    "source_effects": {
                        "type": "create-entity",
                        "entity_name": "explosion-hit"
                    }
                }
            }
        },
        "subgroup": "ammo",
        "order": "d[rocket-launcher]-c[atomic-bomb]",
        "stack_size": 10
    },
    "piercing-shotgun-shell": {
        "type": "ammo",
        "name": "piercing-shotgun-shell",
        "icon": "__base__/graphics/icons/piercing-shotgun-shell.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "ammo_type": {
            "category": "shotgun-shell",
            "target_type": "direction",
            "clamp_position": True,
            "action": [
                {
                    "type": "direct",
                    "action_delivery": {
                        "type": "instant",
                        "source_effects": [
                            {
                                "type": "create-explosion",
                                "entity_name": "explosion-gunshot"
                            }
                        ]
                    }
                },
                {
                    "type": "direct",
                    "repeat_count": 16,
                    "action_delivery": {
                        "type": "projectile",
                        "projectile": "piercing-shotgun-pellet",
                        "starting_speed": 1,
                        "starting_speed_deviation": 0.1,
                        "direction_deviation": 0.3,
                        "range_deviation": 0.3,
                        "max_range": 15
                    }
                }
            ]
        },
        "magazine_size": 10,
        "subgroup": "ammo",
        "order": "b[shotgun]-b[piercing]",
        "stack_size": 200
    },
    "cannon-shell": {
        "type": "ammo",
        "name": "cannon-shell",
        "icon": "__base__/graphics/icons/cannon-shell.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "ammo_type": {
            "category": "cannon-shell",
            "target_type": "direction",
            "action": {
                "type": "direct",
                "action_delivery": {
                    "type": "projectile",
                    "projectile": "cannon-projectile",
                    "starting_speed": 1,
                    "direction_deviation": 0.1,
                    "range_deviation": 0.1,
                    "max_range": 30,
                    "min_range": 5,
                    "source_effects": {
                        "type": "create-explosion",
                        "entity_name": "explosion-gunshot"
                    }
                }
            }
        },
        "subgroup": "ammo",
        "order": "d[cannon-shell]-a[basic]",
        "stack_size": 200
    },
    "explosive-cannon-shell": {
        "type": "ammo",
        "name": "explosive-cannon-shell",
        "icon": "__base__/graphics/icons/explosive-cannon-shell.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "ammo_type": {
            "category": "cannon-shell",
            "target_type": "direction",
            "action": {
                "type": "direct",
                "action_delivery": {
                    "type": "projectile",
                    "projectile": "explosive-cannon-projectile",
                    "starting_speed": 1,
                    "direction_deviation": 0.1,
                    "range_deviation": 0.1,
                    "max_range": 30,
                    "min_range": 5,
                    "source_effects": {
                        "type": "create-explosion",
                        "entity_name": "explosion-gunshot"
                    }
                }
            }
        },
        "subgroup": "ammo",
        "order": "d[cannon-shell]-c[explosive]",
        "stack_size": 200
    },
    "uranium-cannon-shell": {
        "type": "ammo",
        "name": "uranium-cannon-shell",
        "icon": "__base__/graphics/icons/uranium-cannon-shell.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "pictures": {
            "layers": [
                {
                    "size": 64,
                    "filename": "__base__/graphics/icons/uranium-cannon-shell.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                },
                {
                    "draw_as_light": True,
                    "flags": [
                        "light"
                    ],
                    "size": 64,
                    "filename": "__base__/graphics/icons/uranium-cannon-shell-light.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                }
            ]
        },
        "ammo_type": {
            "category": "cannon-shell",
            "target_type": "direction",
            "action": {
                "type": "direct",
                "action_delivery": {
                    "type": "projectile",
                    "projectile": "uranium-cannon-projectile",
                    "starting_speed": 1,
                    "direction_deviation": 0.1,
                    "range_deviation": 0.1,
                    "max_range": 30,
                    "min_range": 5,
                    "source_effects": {
                        "type": "create-explosion",
                        "entity_name": "explosion-gunshot"
                    }
                }
            }
        },
        "subgroup": "ammo",
        "order": "d[cannon-shell]-c[uranium]",
        "stack_size": 200
    },
    "explosive-uranium-cannon-shell": {
        "type": "ammo",
        "name": "explosive-uranium-cannon-shell",
        "icon": "__base__/graphics/icons/explosive-uranium-cannon-shell.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "pictures": {
            "layers": [
                {
                    "size": 64,
                    "filename": "__base__/graphics/icons/explosive-uranium-cannon-shell.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                },
                {
                    "draw_as_light": True,
                    "flags": [
                        "light"
                    ],
                    "size": 64,
                    "filename": "__base__/graphics/icons/uranium-cannon-shell-light.png",
                    "scale": 0.25,
                    "mipmap_count": 4
                }
            ]
        },
        "ammo_type": {
            "category": "cannon-shell",
            "target_type": "direction",
            "action": {
                "type": "direct",
                "action_delivery": {
                    "type": "projectile",
                    "projectile": "explosive-uranium-cannon-projectile",
                    "starting_speed": 1,
                    "direction_deviation": 0.1,
                    "range_deviation": 0.1,
                    "max_range": 30,
                    "min_range": 5,
                    "source_effects": {
                        "type": "create-explosion",
                        "entity_name": "explosion-gunshot"
                    }
                }
            }
        },
        "subgroup": "ammo",
        "order": "d[explosive-cannon-shell]-c[uranium]",
        "stack_size": 200
    },
    "artillery-shell": {
        "type": "ammo",
        "name": "artillery-shell",
        "icon": "__base__/graphics/icons/artillery-shell.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "ammo_type": {
            "category": "artillery-shell",
            "target_type": "position",
            "action": {
                "type": "direct",
                "action_delivery": {
                    "type": "artillery",
                    "projectile": "artillery-projectile",
                    "starting_speed": 1,
                    "direction_deviation": 0,
                    "range_deviation": 0,
                    "source_effects": {
                        "type": "create-explosion",
                        "entity_name": "artillery-cannon-muzzle-flash"
                    }
                }
            }
        },
        "subgroup": "ammo",
        "order": "d[explosive-cannon-shell]-d[artillery]",
        "stack_size": 1
    },
    "flamethrower": {
        "type": "gun",
        "name": "flamethrower",
        "icon": "__base__/graphics/icons/flamethrower.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "order": "e[flamethrower]",
        "attack_parameters": {
            "type": "stream",
            "ammo_category": "flamethrower",
            "cooldown": 1,
            "movement_slow_down_factor": 0.4,
            "gun_barrel_length": 0.8,
            "gun_center_shift": [
                0,
                -1
            ],
            "range": 15,
            "min_range": 3,
            "cyclic_sound": {
                "begin_sound": [
                    {
                        "filename": "__base__/sound/fight/flamethrower-start.ogg",
                        "volume": 0.7
                    }
                ],
                "middle_sound": [
                    {
                        "filename": "__base__/sound/fight/flamethrower-mid.ogg",
                        "volume": 0.7
                    }
                ],
                "end_sound": [
                    {
                        "filename": "__base__/sound/fight/flamethrower-end.ogg",
                        "volume": 0.7
                    }
                ]
            }
        },
        "stack_size": 5
    },
    "tank-machine-gun": {
        "type": "gun",
        "name": "tank-machine-gun",
        "icon": "__base__/graphics/icons/submachine-gun.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "gun",
        "order": "a[basic-clips]-b[tank-machine-gun]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "bullet",
            "cooldown": 4,
            "movement_slow_down_factor": 0.7,
            "shell_particle": {
                "name": "shell-particle",
                "direction_deviation": 0.1,
                "speed": 0.1,
                "speed_deviation": 0.03,
                "center": [
                    0,
                    0
                ],
                "creation_distance": -0.6875,
                "starting_frame_speed": 0.4,
                "starting_frame_speed_deviation": 0.1
            },
            "projectile_center": [
                -0.15625,
                -0.07812
            ],
            "projectile_creation_distance": 1,
            "range": 20,
            "sound": "sounds",
            "9": ".heavy_gunshot"
        },
        "stack_size": 1
    },
    "tank-flamethrower": {
        "type": "gun",
        "name": "tank-flamethrower",
        "icon": "__base__/graphics/icons/flamethrower.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "gun",
        "order": "b[flamethrower]-b[tank-flamethrower]",
        "attack_parameters": {
            "type": "stream",
            "ammo_category": "flamethrower",
            "cooldown": 1,
            "gun_barrel_length": 1.4,
            "gun_center_shift": [
                -0.17,
                -1.15
            ],
            "range": 9,
            "min_range": 3,
            "cyclic_sound": {
                "begin_sound": [
                    {
                        "filename": "__base__/sound/fight/flamethrower-start.ogg",
                        "volume": 1
                    }
                ],
                "middle_sound": [
                    {
                        "filename": "__base__/sound/fight/flamethrower-mid.ogg",
                        "volume": 1
                    }
                ],
                "end_sound": [
                    {
                        "filename": "__base__/sound/fight/flamethrower-end.ogg",
                        "volume": 1
                    }
                ]
            }
        },
        "stack_size": 1
    },
    "land-mine": {
        "type": "item_dict",
        "name": "land-mine",
        "icon": "__base__/graphics/icons/land-mine.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "order": "f[land-mine]",
        "place_result": "land-mine",
        "stack_size": 100
    },
    "rocket-launcher": {
        "type": "gun",
        "name": "rocket-launcher",
        "icon": "__base__/graphics/icons/rocket-launcher.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "order": "d[rocket-launcher]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "rocket",
            "movement_slow_down_factor": 0.8,
            "cooldown": 60,
            "projectile_creation_distance": 0.6,
            "range": 36,
            "projectile_center": [
                -0.17,
                0
            ],
            "sound": [
                {
                    "filename": "__base__/sound/fight/rocket-launcher.ogg",
                    "volume": 0.7
                }
            ]
        },
        "stack_size": 5
    },
    "combat-shotgun": {
        "type": "gun",
        "name": "combat-shotgun",
        "icon": "__base__/graphics/icons/combat-shotgun.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "order": "b[shotgun]-a[combat]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "shotgun-shell",
            "cooldown": 30,
            "movement_slow_down_factor": 0.5,
            "damage_modifier": 1.2,
            "projectile_creation_distance": 1.125,
            "range": 15,
            "sound": "sounds",
            "8": ".shotgun"
        },
        "stack_size": 5
    },
    "tank-cannon": {
        "type": "gun",
        "name": "tank-cannon",
        "icon": "__base__/graphics/icons/tank-cannon.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "gun",
        "order": "z[tank]-a[cannon]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "cannon-shell",
            "cooldown": 90,
            "movement_slow_down_factor": 0,
            "projectile_creation_distance": 1.6,
            "projectile_center": [
                -0.15625,
                -0.07812
            ],
            "range": 25,
            "sound": "sounds",
            "8": ".tank_gunshot"
        },
        "stack_size": 5
    },
    "artillery-wagon-cannon": {
        "type": "gun",
        "name": "artillery-wagon-cannon",
        "icon": "__base__/graphics/icons/tank-cannon.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "gun",
        "order": "z[artillery]-a[cannon]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "artillery-shell",
            "cooldown": 200,
            "movement_slow_down_factor": 0,
            "projectile_creation_distance": 1.6,
            "projectile_center": [
                -0.15625,
                -0.07812
            ],
            "range": 7,
            "7": 32,
            "min_range": 1,
            "9": 32,
            "projectile_creation_parameters": "require",
            "11": ")",
            "sound": [
                {
                    "filename": "__base__/sound/fight/artillery-shoots-1.ogg",
                    "volume": 0.7
                }
            ],
            "shell_particle": {
                "name": "artillery-shell-particle",
                "direction_deviation": 0.05,
                "direction": 0.4,
                "speed": 0.1,
                "speed_deviation": 0.1,
                "vertical_speed": 0.05,
                "vertical_speed_deviation": 0.01,
                "center": [
                    0,
                    -0.5
                ],
                "creation_distance": 0.5,
                "creation_distance_orientation": 0.4,
                "starting_frame_speed": 0.5,
                "starting_frame_speed_deviation": 0.5,
                "use_source_position": True,
                "height": 1
            }
        },
        "stack_size": 1
    },
    "spidertron-rocket-launcher-1": {
        "type": "gun",
        "name": "spidertron-rocket-launcher-1",
        "localised_name": [
            "item_dict-name.spidertron-rocket-launcher"
        ],
        "icon": "__base__/graphics/icons/rocket-launcher.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "flags": [
            "hidden"
        ],
        "order": "z[spider]-a[rocket-launcher]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "rocket",
            "cooldown": 60,
            "range": 36,
            "projectile_creation_distance": -0.5,
            "projectile_center": [
                0,
                0.3
            ],
            "projectile_orientation_offset": -0.0625,
            "sound": [
                {
                    "filename": "__base__/sound/fight/rocket-launcher.ogg",
                    "volume": 0.7
                }
            ]
        },
        "stack_size": 1
    },
    "spidertron-rocket-launcher-2": {
        "type": "gun",
        "name": "spidertron-rocket-launcher-2",
        "localised_name": [
            "item_dict-name.spidertron-rocket-launcher"
        ],
        "icon": "__base__/graphics/icons/rocket-launcher.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "flags": [
            "hidden"
        ],
        "order": "z[spider]-a[rocket-launcher]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "rocket",
            "cooldown": 60,
            "range": 36,
            "projectile_creation_distance": -0.5,
            "projectile_orientation_offset": -0.03125,
            "projectile_center": [
                0,
                0.3
            ],
            "sound": [
                {
                    "filename": "__base__/sound/fight/rocket-launcher.ogg",
                    "volume": 0.7
                }
            ]
        },
        "stack_size": 1
    },
    "spidertron-rocket-launcher-3": {
        "type": "gun",
        "name": "spidertron-rocket-launcher-3",
        "localised_name": [
            "item_dict-name.spidertron-rocket-launcher"
        ],
        "icon": "__base__/graphics/icons/rocket-launcher.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "flags": [
            "hidden"
        ],
        "order": "z[spider]-a[rocket-launcher]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "rocket",
            "cooldown": 60,
            "range": 36,
            "projectile_creation_distance": -0.5,
            "projectile_center": [
                0,
                0.3
            ],
            "projectile_orientation_offset": 0.03125,
            "sound": [
                {
                    "filename": "__base__/sound/fight/rocket-launcher.ogg",
                    "volume": 0.7
                }
            ]
        },
        "stack_size": 1
    },
    "spidertron-rocket-launcher-4": {
        "type": "gun",
        "name": "spidertron-rocket-launcher-4",
        "localised_name": [
            "item_dict-name.spidertron-rocket-launcher"
        ],
        "icon": "__base__/graphics/icons/rocket-launcher.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "flags": [
            "hidden"
        ],
        "order": "z[spider]-a[rocket-launcher]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "rocket",
            "cooldown": 60,
            "range": 36,
            "projectile_creation_distance": -0.5,
            "projectile_center": [
                0,
                0.3
            ],
            "projectile_orientation_offset": 0.0625,
            "sound": [
                {
                    "filename": "__base__/sound/fight/rocket-launcher.ogg",
                    "volume": 0.7
                }
            ]
        },
        "stack_size": 1
    },
    "power-armor": {
        "type": "armor",
        "name": "power-armor",
        "icon": "__base__/graphics/icons/power-armor.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "resistances": [
            {
                "type": "physical",
                "decrease": 8,
                "percent": 30
            },
            {
                "type": "acid",
                "decrease": 0,
                "percent": 60
            },
            {
                "type": "explosion",
                "decrease": 40,
                "percent": 40
            },
            {
                "type": "fire",
                "decrease": 0,
                "percent": 60
            }
        ],
        "subgroup": "armor",
        "order": "d[power-armor]",
        "stack_size": 1,
        "infinite": True,
        "equipment_grid": "medium-equipment-grid",
        "inventory_size_bonus": 20,
        "open_sound": {
            "filename": "__base__/sound/armor-open.ogg",
            "volume": 1
        },
        "close_sound": {
            "filename": "__base__/sound/armor-close.ogg",
            "volume": 1
        }
    },
    "power-armor-mk2": {
        "type": "armor",
        "name": "power-armor-mk2",
        "icon": "__base__/graphics/icons/power-armor-mk2.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "resistances": [
            {
                "type": "physical",
                "decrease": 10,
                "percent": 40
            },
            {
                "type": "acid",
                "decrease": 0,
                "percent": 70
            },
            {
                "type": "explosion",
                "decrease": 60,
                "percent": 50
            },
            {
                "type": "fire",
                "decrease": 0,
                "percent": 70
            }
        ],
        "subgroup": "armor",
        "order": "e[power-armor-mk2]",
        "stack_size": 1,
        "infinite": True,
        "equipment_grid": "large-equipment-grid",
        "inventory_size_bonus": 30,
        "open_sound": {
            "filename": "__base__/sound/armor-open.ogg",
            "volume": 1
        },
        "close_sound": {
            "filename": "__base__/sound/armor-close.ogg",
            "volume": 1
        }
    },
    "poison-capsule": {
        "type": "capsule",
        "name": "poison-capsule",
        "icon": "__base__/graphics/icons/poison-capsule.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "capsule_action": {
            "type": "throw",
            "attack_parameters": {
                "type": "projectile",
                "activation_type": "throw",
                "ammo_category": "capsule",
                "cooldown": 30,
                "projectile_creation_distance": 0.6,
                "range": 25,
                "ammo_type": {
                    "category": "capsule",
                    "target_type": "position",
                    "action": [
                        {
                            "type": "direct",
                            "action_delivery": {
                                "type": "projectile",
                                "projectile": "poison-capsule",
                                "starting_speed": 0.3
                            }
                        },
                        {
                            "type": "direct",
                            "action_delivery": {
                                "type": "instant",
                                "target_effects": [
                                    {
                                        "type": "play-sound",
                                        "sound": "sounds",
                                        "2": ".throw_projectile"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        },
        "subgroup": "capsule",
        "order": "b[poison-capsule]",
        "stack_size": 100
    },
    "distractor-capsule": {
        "type": "capsule",
        "name": "distractor-capsule",
        "icon": "__base__/graphics/icons/distractor.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "capsule_action": {
            "type": "throw",
            "attack_parameters": {
                "type": "projectile",
                "activation_type": "throw",
                "ammo_category": "capsule",
                "cooldown": 30,
                "projectile_creation_distance": 0.6,
                "range": 25,
                "ammo_type": {
                    "category": "capsule",
                    "target_type": "position",
                    "action": [
                        {
                            "type": "direct",
                            "action_delivery": {
                                "type": "projectile",
                                "projectile": "distractor-capsule",
                                "starting_speed": 0.3
                            }
                        },
                        {
                            "type": "direct",
                            "action_delivery": {
                                "type": "instant",
                                "target_effects": [
                                    {
                                        "type": "play-sound",
                                        "sound": "sounds",
                                        "2": ".throw_projectile"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        },
        "subgroup": "capsule",
        "order": "e[defender-capsule]",
        "stack_size": 100
    },
    "destroyer-capsule": {
        "type": "capsule",
        "name": "destroyer-capsule",
        "icon": "__base__/graphics/icons/destroyer.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "capsule_action": {
            "type": "throw",
            "attack_parameters": {
                "type": "projectile",
                "activation_type": "throw",
                "ammo_category": "capsule",
                "cooldown": 30,
                "projectile_creation_distance": 0.6,
                "range": 25,
                "ammo_type": {
                    "category": "capsule",
                    "target_type": "position",
                    "action": [
                        {
                            "type": "direct",
                            "action_delivery": {
                                "type": "projectile",
                                "projectile": "destroyer-capsule",
                                "starting_speed": 0.3
                            }
                        },
                        {
                            "type": "direct",
                            "action_delivery": {
                                "type": "instant",
                                "target_effects": [
                                    {
                                        "type": "play-sound",
                                        "sound": "sounds",
                                        "2": ".throw_projectile"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        },
        "subgroup": "capsule",
        "order": "f[destroyer-capsule]",
        "stack_size": 100
    },
    "cliff-explosives": {
        "type": "capsule",
        "name": "cliff-explosives",
        "icon": "__base__/graphics/icons/cliff-explosives.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hide-from-bonus-gui"
        ],
        "capsule_action": {
            "type": "destroy-cliffs",
            "radius": 1.5,
            "attack_parameters": {
                "type": "projectile",
                "activation_type": "throw",
                "ammo_category": "grenade",
                "cooldown": 30,
                "projectile_creation_distance": 0.6,
                "range": 10,
                "ammo_type": {
                    "category": "grenade",
                    "target_type": "position",
                    "action": {
                        "type": "direct",
                        "action_delivery": {
                            "type": "projectile",
                            "projectile": "cliff-explosives",
                            "starting_speed": 0.3
                        }
                    }
                }
            }
        },
        "subgroup": "terrain",
        "order": "d[cliff-explosives]",
        "stack_size": 20
    },
    "firearm-magazine": {
        "type": "ammo",
        "name": "firearm-magazine",
        "icon": "__base__/graphics/icons/firearm-magazine.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "ammo_type": {
            "category": "bullet",
            "action": [
                {
                    "type": "direct",
                    "action_delivery": [
                        {
                            "type": "instant",
                            "source_effects": [
                                {
                                    "type": "create-explosion",
                                    "entity_name": "explosion-gunshot"
                                }
                            ],
                            "target_effects": [
                                {
                                    "type": "create-entity",
                                    "entity_name": "explosion-hit",
                                    "offsets": [
                                        [
                                            0,
                                            1
                                        ]
                                    ],
                                    "offset_deviation": [
                                        [
                                            -0.5,
                                            -0.5
                                        ],
                                        [
                                            0.5,
                                            0.5
                                        ]
                                    ]
                                },
                                {
                                    "type": "damage",
                                    "damage": {
                                        "amount": 5,
                                        "type": "physical"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        "magazine_size": 10,
        "subgroup": "ammo",
        "order": "a[basic-clips]-a[firearm-magazine]",
        "stack_size": 200
    },
    "piercing-rounds-magazine": {
        "type": "ammo",
        "name": "piercing-rounds-magazine",
        "icon": "__base__/graphics/icons/piercing-rounds-magazine.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "ammo_type": {
            "category": "bullet",
            "action": {
                "type": "direct",
                "action_delivery": {
                    "type": "instant",
                    "source_effects": {
                        "type": "create-explosion",
                        "entity_name": "explosion-gunshot"
                    },
                    "target_effects": [
                        {
                            "type": "create-entity",
                            "entity_name": "explosion-hit",
                            "offsets": [
                                [
                                    0,
                                    1
                                ]
                            ],
                            "offset_deviation": [
                                [
                                    -0.5,
                                    -0.5
                                ],
                                [
                                    0.5,
                                    0.5
                                ]
                            ]
                        },
                        {
                            "type": "damage",
                            "damage": {
                                "amount": 8,
                                "type": "physical"
                            }
                        }
                    ]
                }
            }
        },
        "magazine_size": 10,
        "subgroup": "ammo",
        "order": "a[basic-clips]-b[piercing-rounds-magazine]",
        "stack_size": 200
    },
    "shotgun-shell": {
        "type": "ammo",
        "name": "shotgun-shell",
        "icon": "__base__/graphics/icons/shotgun-shell.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "ammo_type": {
            "category": "shotgun-shell",
            "target_type": "direction",
            "clamp_position": True,
            "action": [
                {
                    "type": "direct",
                    "action_delivery": {
                        "type": "instant",
                        "source_effects": [
                            {
                                "type": "create-explosion",
                                "entity_name": "explosion-gunshot"
                            }
                        ]
                    }
                },
                {
                    "type": "direct",
                    "repeat_count": 12,
                    "action_delivery": {
                        "type": "projectile",
                        "projectile": "shotgun-pellet",
                        "starting_speed": 1,
                        "starting_speed_deviation": 0.1,
                        "direction_deviation": 0.3,
                        "range_deviation": 0.3,
                        "max_range": 15
                    }
                }
            ]
        },
        "magazine_size": 10,
        "subgroup": "ammo",
        "order": "b[shotgun]-a[basic]",
        "stack_size": 200
    },
    "light-armor": {
        "type": "armor",
        "name": "light-armor",
        "icon": "__base__/graphics/icons/light-armor.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "resistances": [
            {
                "type": "physical",
                "decrease": 3,
                "percent": 20
            },
            {
                "type": "acid",
                "decrease": 0,
                "percent": 20
            },
            {
                "type": "explosion",
                "decrease": 2,
                "percent": 20
            },
            {
                "type": "fire",
                "decrease": 0,
                "percent": 10
            }
        ],
        "subgroup": "armor",
        "order": "a[light-armor]",
        "stack_size": 1,
        "infinite": True
    },
    "heavy-armor": {
        "type": "armor",
        "name": "heavy-armor",
        "icon": "__base__/graphics/icons/heavy-armor.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "resistances": [
            {
                "type": "physical",
                "decrease": 6,
                "percent": 30
            },
            {
                "type": "explosion",
                "decrease": 20,
                "percent": 30
            },
            {
                "type": "acid",
                "decrease": 0,
                "percent": 40
            },
            {
                "type": "fire",
                "decrease": 0,
                "percent": 30
            }
        ],
        "subgroup": "armor",
        "order": "b[heavy-armor]",
        "stack_size": 1,
        "infinite": True
    },
    "pistol": {
        "type": "gun",
        "name": "pistol",
        "icon": "__base__/graphics/icons/pistol.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "order": "a[basic-clips]-a[pistol]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "bullet",
            "cooldown": 15,
            "movement_slow_down_factor": 0.2,
            "shell_particle": {
                "name": "shell-particle",
                "direction_deviation": 0.1,
                "speed": 0.1,
                "speed_deviation": 0.03,
                "center": [
                    0,
                    0.1
                ],
                "creation_distance": -0.5,
                "starting_frame_speed": 0.4,
                "starting_frame_speed_deviation": 0.1
            },
            "projectile_creation_distance": 1.125,
            "range": 15,
            "sound": "sounds",
            "8": ".light_gunshot"
        },
        "stack_size": 5
    },
    "submachine-gun": {
        "type": "gun",
        "name": "submachine-gun",
        "icon": "__base__/graphics/icons/submachine-gun.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "order": "a[basic-clips]-b[submachine-gun]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "bullet",
            "cooldown": 6,
            "movement_slow_down_factor": 0.7,
            "shell_particle": {
                "name": "shell-particle",
                "direction_deviation": 0.1,
                "speed": 0.1,
                "speed_deviation": 0.03,
                "center": [
                    0,
                    0.1
                ],
                "creation_distance": -0.5,
                "starting_frame_speed": 0.4,
                "starting_frame_speed_deviation": 0.1
            },
            "projectile_creation_distance": 1.125,
            "range": 18,
            "sound": "sounds",
            "8": ".submachine_gunshot"
        },
        "stack_size": 5
    },
    "vehicle-machine-gun": {
        "type": "gun",
        "name": "vehicle-machine-gun",
        "icon": "__base__/graphics/icons/submachine-gun.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "flags": [
            "hidden"
        ],
        "subgroup": "gun",
        "order": "a[basic-clips]-b[vehicle-machine-gun]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "bullet",
            "cooldown": 4,
            "movement_slow_down_factor": 0.7,
            "shell_particle": {
                "name": "shell-particle",
                "direction_deviation": 0.1,
                "speed": 0.1,
                "speed_deviation": 0.03,
                "center": [
                    0,
                    0
                ],
                "creation_distance": -0.6875,
                "starting_frame_speed": 0.4,
                "starting_frame_speed_deviation": 0.1
            },
            "projectile_creation_distance": 0.65,
            "range": 20,
            "sound": "sounds",
            "8": ".heavy_gunshot"
        },
        "stack_size": 1
    },
    "shotgun": {
        "type": "gun",
        "name": "shotgun",
        "icon": "__base__/graphics/icons/shotgun.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "gun",
        "order": "b[shotgun]-a[basic]",
        "attack_parameters": {
            "type": "projectile",
            "ammo_category": "shotgun-shell",
            "cooldown": 60,
            "movement_slow_down_factor": 0.6,
            "projectile_creation_distance": 1.125,
            "range": 15,
            "min_range": 1,
            "sound": "sounds",
            "8": ".shotgun"
        },
        "stack_size": 5
    },
    "fusion-reactor-equipment": {
        "type": "item_dict",
        "name": "fusion-reactor-equipment",
        "icon": "__base__/graphics/icons/fusion-reactor-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "fusion-reactor-equipment",
        "subgroup": "equipment",
        "order": "a[energy-source]-b[fusion-reactor]",
        "default_request_amount": 1,
        "stack_size": 20
    },
    "battery-equipment": {
        "type": "item_dict",
        "name": "battery-equipment",
        "icon": "__base__/graphics/icons/battery-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "battery-equipment",
        "subgroup": "equipment",
        "order": "b[battery]-a[battery-equipment]",
        "default_request_amount": 5,
        "stack_size": 20
    },
    "battery-mk2-equipment": {
        "type": "item_dict",
        "name": "battery-mk2-equipment",
        "localised_description": [
            "item_dict-description.battery-equipment"
        ],
        "icon": "__base__/graphics/icons/battery-mk2-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "battery-mk2-equipment",
        "subgroup": "equipment",
        "order": "b[battery]-b[battery-equipment-mk2]",
        "default_request_amount": 5,
        "stack_size": 20
    },
    "belt-immunity-equipment": {
        "type": "item_dict",
        "name": "belt-immunity-equipment",
        "icon": "__base__/graphics/icons/belt-immunity-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "belt-immunity-equipment",
        "subgroup": "equipment",
        "order": "c[belt-immunity]-a[belt-immunity]",
        "default_request_amount": 1,
        "stack_size": 20
    },
    "exoskeleton-equipment": {
        "type": "item_dict",
        "name": "exoskeleton-equipment",
        "icon": "__base__/graphics/icons/exoskeleton-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "exoskeleton-equipment",
        "subgroup": "equipment",
        "order": "d[exoskeleton]-a[exoskeleton-equipment]",
        "default_request_amount": 5,
        "stack_size": 20
    },
    "personal-roboport-equipment": {
        "type": "item_dict",
        "name": "personal-roboport-equipment",
        "icon": "__base__/graphics/icons/personal-roboport-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "personal-roboport-equipment",
        "subgroup": "equipment",
        "order": "e[robotics]-a[personal-roboport-equipment]",
        "default_request_amount": 1,
        "stack_size": 20
    },
    "personal-roboport-mk2-equipment": {
        "type": "item_dict",
        "name": "personal-roboport-mk2-equipment",
        "localised_description": [
            "item_dict-description.personal-roboport-equipment"
        ],
        "icon": "__base__/graphics/icons/personal-roboport-mk2-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "personal-roboport-mk2-equipment",
        "subgroup": "equipment",
        "order": "e[robotics]-b[personal-roboport-mk2-equipment]",
        "default_request_amount": 1,
        "stack_size": 20
    },
    "night-vision-equipment": {
        "type": "item_dict",
        "name": "night-vision-equipment",
        "icon": "__base__/graphics/icons/night-vision-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "night-vision-equipment",
        "subgroup": "equipment",
        "order": "f[night-vision]-a[night-vision-equipment]",
        "default_request_amount": 1,
        "stack_size": 20
    },
    "energy-shield-equipment": {
        "type": "item_dict",
        "name": "energy-shield-equipment",
        "icon": "__base__/graphics/icons/energy-shield-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "energy-shield-equipment",
        "subgroup": "military-equipment",
        "order": "a[shield]-a[energy-shield-equipment]",
        "default_request_amount": 5,
        "stack_size": 20
    },
    "energy-shield-mk2-equipment": {
        "type": "item_dict",
        "name": "energy-shield-mk2-equipment",
        "localised_description": [
            "item_dict-description.energy-shield-equipment"
        ],
        "icon": "__base__/graphics/icons/energy-shield-mk2-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "energy-shield-mk2-equipment",
        "subgroup": "military-equipment",
        "order": "a[shield]-b[energy-shield-equipment-mk2]",
        "default_request_amount": 5,
        "stack_size": 20
    },
    "personal-laser-defense-equipment": {
        "type": "item_dict",
        "name": "personal-laser-defense-equipment",
        "icon": "__base__/graphics/icons/personal-laser-defense-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "personal-laser-defense-equipment",
        "subgroup": "military-equipment",
        "order": "b[active-defense]-a[personal-laser-defense-equipment]",
        "default_request_amount": 5,
        "stack_size": 20
    },
    "discharge-defense-equipment": {
        "type": "item_dict",
        "name": "discharge-defense-equipment",
        "icon": "__base__/graphics/icons/discharge-defense-equipment.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "placed_as_equipment_result": "discharge-defense-equipment",
        "subgroup": "military-equipment",
        "order": "b[active-defense]-b[discharge-defense-equipment]-a[equipment]",
        "default_request_amount": 1,
        "stack_size": 20
    },
    "discharge-defense-remote": {
        "type": "capsule",
        "name": "discharge-defense-remote",
        "icon": "__base__/graphics/icons/discharge-defense-equipment-controller.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "capsule_action": {
            "type": "equipment-remote",
            "equipment": "discharge-defense-equipment"
        },
        "subgroup": "military-equipment",
        "order": "b[active-defense]-b[discharge-defense-equipment]-b[remote]",
        "stack_size": 1
    },
    "gun-turret": {
        "type": "item_dict",
        "name": "gun-turret",
        "icon": "__base__/graphics/icons/gun-turret.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "defensive-structure",
        "order": "b[turret]-a[gun-turret]",
        "place_result": "gun-turret",
        "stack_size": 50
    },
    "laser-turret": {
        "type": "item_dict",
        "name": "laser-turret",
        "icon": "__base__/graphics/icons/laser-turret.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "defensive-structure",
        "order": "b[turret]-b[laser-turret]",
        "place_result": "laser-turret",
        "stack_size": 50
    },
    "flamethrower-turret": {
        "type": "item_dict",
        "name": "flamethrower-turret",
        "icon": "__base__/graphics/icons/flamethrower-turret.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "defensive-structure",
        "order": "b[turret]-c[flamethrower-turret]",
        "place_result": "flamethrower-turret",
        "stack_size": 50
    },
    "artillery-turret": {
        "type": "item_dict",
        "name": "artillery-turret",
        "icon": "__base__/graphics/icons/artillery-turret.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "defensive-structure",
        "order": "b[turret]-d[artillery-turret]-a[turret]",
        "place_result": "artillery-turret",
        "stack_size": 10
    },
    "artillery-targeting-remote": {
        "type": "capsule",
        "name": "artillery-targeting-remote",
        "icon": "__base__/graphics/icons/artillery-targeting-remote.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "capsule_action": {
            "type": "artillery-remote",
            "flare": "artillery-flare"
        },
        "subgroup": "defensive-structure",
        "order": "b[turret]-d[artillery-turret]-b[remote]",
        "stack_size": 1
    },
    "decider-combinator": {
        "type": "item_dict",
        "name": "decider-combinator",
        "icon": "__base__/graphics/icons/decider-combinator.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "circuit-network",
        "place_result": "decider-combinator",
        "order": "c[combinators]-b[decider-combinator]",
        "stack_size": 50
    },
    "constant-combinator": {
        "type": "item_dict",
        "name": "constant-combinator",
        "icon": "__base__/graphics/icons/constant-combinator.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "circuit-network",
        "place_result": "constant-combinator",
        "order": "c[combinators]-c[constant-combinator]",
        "stack_size": 50
    },
    "power-switch": {
        "type": "item_dict",
        "name": "power-switch",
        "icon": "__base__/graphics/icons/power-switch.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "circuit-network",
        "place_result": "power-switch",
        "order": "d[other]-a[power-switch]",
        "stack_size": 50
    },
    "programmable-speaker": {
        "type": "item_dict",
        "name": "programmable-speaker",
        "icon": "__base__/graphics/icons/programmable-speaker.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "subgroup": "circuit-network",
        "order": "d[other]-b[programmable-speaker]",
        "place_result": "programmable-speaker",
        "stack_size": 50
    },
    "dummy-steel-axe": {
        "type": "mining-tool",
        "name": "dummy-steel-axe",
        "icon": "__base__/graphics/icons/steel-axe.png",
        "icon_size": 64,
        "icon_mipmaps": 4,
        "durability": 1,
        "subgroup": "tool",
        "order": "a[mining]-b[steel-axe]",
        "flags": [
            "hidden"
        ],
        "stack_size": 1
    }
}
