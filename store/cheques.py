from ..__config__ import CONFIGURATION
from ..__exceptions__ import APIError
from ..scripts.sender import create_session
from ..scripts import j2


async def get(chequeID: str) -> dict[str, ...]:
    """
    Запрос данных о чеке в следующем формате:
    | {
    | "chequeID": str,
    | "storeID": str,
    | "customer": int,
    | "unix": float,
    | "items": dict[itemID (str) : multiplier (int)],
    | "active": bool
    | }

    :param chequeID: ID чека
    :return: словарь с данными чека из таблицы ``database.CHEQUES``
    """

    async with create_session() as session:
        async with session.get(
                f"{CONFIGURATION.PROXY}/store/cheques/get",
                params={"chequeID": chequeID}
        ) as response:
            json = await response.json()
            if response.status >= 400:
                raise APIError.get(get, response.status, json)

            json["items"] = j2.from_(json["items"])
            return json
