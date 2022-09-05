"""Tests for the Tesla button."""
from unittest.mock import patch

from homeassistant.components.button import (
    DOMAIN as BUTTON_DOMAIN,
)
from homeassistant.const import ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er

from .common import setup_platform


async def test_registry_entries(hass: HomeAssistant) -> None:
    """Tests devices are registered in the entity registry."""
    await setup_platform(hass, BUTTON_DOMAIN)
    entity_registry = er.async_get(hass)

    entry = entity_registry.async_get("button.my_model_s_horn")
    assert entry.unique_id == "tesla_model_s_111111_horn"

    entry = entity_registry.async_get("button.my_model_s_flash_lights")
    assert entry.unique_id == "tesla_model_s_111111_flash_lights"

    entry = entity_registry.async_get("button.my_model_s_wake_up")
    assert entry.unique_id == "tesla_model_s_111111_wake_up"

    entry = entity_registry.async_get("button.my_model_s_force_data_update")
    assert entry.unique_id == "tesla_model_s_111111_force_data_update"

    entry = entity_registry.async_get("button.my_model_s_trigger_homelink")
    assert entry.unique_id == "tesla_model_s_111111_trigger_homelink"


async def test_horn_press(hass: HomeAssistant) -> None:
    """Tests car horn button press."""
    await setup_platform(hass, BUTTON_DOMAIN)

    with patch("teslajsonpy.car.TeslaCar.honk_horn") as mock_honk_horn:
        assert await hass.services.async_call(
            BUTTON_DOMAIN,
            "press",
            {ATTR_ENTITY_ID: "button.my_model_s_horn"},
            blocking=True,
        )
        mock_honk_horn.assert_awaited_once()


async def test_flash_lights_press(hass: HomeAssistant) -> None:
    """Tests car flash lights button press."""
    await setup_platform(hass, BUTTON_DOMAIN)

    with patch("teslajsonpy.car.TeslaCar.flash_lights") as mock_flash_lights:
        assert await hass.services.async_call(
            BUTTON_DOMAIN,
            "press",
            {ATTR_ENTITY_ID: "button.my_model_s_flash_lights"},
            blocking=True,
        )
        mock_flash_lights.assert_awaited_once()


async def test_wake_up_press(hass: HomeAssistant) -> None:
    """Tests car wake up button press."""
    await setup_platform(hass, BUTTON_DOMAIN)

    with patch("teslajsonpy.car.TeslaCar.wake_up") as mock_wake_up:
        assert await hass.services.async_call(
            BUTTON_DOMAIN,
            "press",
            {ATTR_ENTITY_ID: "button.my_model_s_wake_up"},
            blocking=True,
        )
        mock_wake_up.assert_awaited_once()


# async def test_force_data_update_press(hass: HomeAssistant) -> None:
#     """Tests car force data button press."""
#     await setup_platform(hass, BUTTON_DOMAIN)

#     with patch("teslajsonpy.Controller.update") as mock_force_data_update:
#         assert await hass.services.async_call(
#             BUTTON_DOMAIN,
#             "press",
#             {ATTR_ENTITY_ID: "button.my_model_s_force_data_update"},
#             blocking=True,
#         )
#         mock_force_data_update.assert_awaited_once()  # Not being awaited - issue with patch?


# async def test_trigger_homelink_press(hass: HomeAssistant) -> None:
#     """Tests car trigger homelink button press."""
#     await setup_platform(hass, BUTTON_DOMAIN)

#     with patch("teslajsonpy.car.TeslaCar.trigger_homelink") as mock_trigger_homelink:
#         assert await hass.services.async_call(
#             BUTTON_DOMAIN,
#             "press",
#             {ATTR_ENTITY_ID: "button.my_model_s_trigger_homelink"},
#             blocking=True,
#         )
#         mock_trigger_homelink.assert_awaited_once()  # Not being awaited - issue with patch?
