from homeassistant.components.switch import SwitchDeviceClass, SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import get_binary_sensor_definitions, DOMAIN, BinarySensorDefinition
from .coordinator import EbyteM31Coordinator
from .entity import EbyteM31Entity
