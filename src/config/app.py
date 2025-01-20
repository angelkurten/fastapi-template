from pydantic import BaseModel, ConfigDict


class AppConfig(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    profiles: list[str]
    debug: bool = False

    def contains_profile(self, profile: str) -> bool:
        return profile in self.profiles
