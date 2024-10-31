from database import Session
from models import User, Role
from utils import hash_password

user_list = [
    {
        "username": "admin_sir",
        "email": "admin.sir@gmail.com",
        "role": Role.PRINCIPAL,
        "password": "admin@sir#"
    },
    {
        "username": "math_teacher",
        "email": "math.teacher@gmail.com",
        "role": Role.MATH_TEACHER,
        "password": "math@teacher#"
    },
    {
        "username": "english_teacher",
        "email": "english.teacher@gmail.com",
        "role": Role.ENGLISH_TEACHER,
        "password": "english@teacher#"
    },
    {
        "username": "science_teacher",
        "email": "science.teacher@gmail.com",
        "role": Role.SCIENCE_TEACHER,
        "password": "science@teacher#"
    },
    {
        "username": "history_teacher",
        "email": "history.teacher@gmail.com",
        "role": Role.HISTORY_TEACHER,
        "password": "history@teacher#"
    },
    {
        "username": "computer_teacher",
        "email": "computer.teacher@gmail.com",
        "role": Role.COMPUTER_TEACHER,
        "password": "computer@teacher#"
    },
    {
        "username": "blue_bird",
        "email": "blue.bird@gmail.com",
        "role": Role.STUDENT,
        "password": "blue@bird#"
    },
    {
        "username": "juju_raven",
        "email": "juju.raven@gmail.com",
        "role": Role.STUDENT,
        "password": "juju@raven#"
    },
    {
        "username": "black_rose",
        "email": "black.rose@gmail.com",
        "role": Role.STUDENT,
        "password": "black@rose#"
    },
    {
        "username": "silver_wolf",
        "email": "silver.wolf@gmail.com",
        "role": Role.STUDENT,
        "password": "silver@wolf#"
    },
    {
        "username": "crimson_tiger",
        "email": "crimson.tiger@gmail.com",
        "role": Role.STUDENT,
        "password": "crimson@tiger#"
    },
    {
        "username": "golden_eagle",
        "email": "golden.eagle@gmail.com",
        "role": Role.STUDENT,
        "password": "golden@eagle#"
    },
    {
        "username": "emerald_falcon",
        "email": "emerald.falcon@gmail.com",
        "role": Role.STUDENT,
        "password": "emerald@falcon#"
    },
    {
        "username": "white_fox",
        "email": "white.fox@gmail.com",
        "role": Role.STUDENT,
        "password": "white@fox#"
    },
    {
        "username": "violet_dove",
        "email": "violet.dove@gmail.com",
        "role": Role.STUDENT,
        "password": "violet@dove#"
    },
    {
        "username": "stormy_sea",
        "email": "stormy.sea@gmail.com",
        "role": Role.STUDENT,
        "password": "stormy@sea#"
    },
    {
        "username": "red_dragon",
        "email": "red.dragon@gmail.com",
        "role": Role.STUDENT,
        "password": "red@dragon#"
    },
    {
        "username": "purple_panther",
        "email": "purple.panther@gmail.com",
        "role": Role.STUDENT,
        "password": "purple@panther#"
    },
    {
        "username": "golden_lion",
        "email": "golden.lion@gmail.com",
        "role": Role.STUDENT,
        "password": "golden@lion#"
    },
    {
        "username": "gray_wolf",
        "email": "gray.wolf@gmail.com",
        "role": Role.STUDENT,
        "password": "gray@wolf#"
    },
    {
        "username": "icy_owl",
        "email": "icy.owl@gmail.com",
        "role": Role.STUDENT,
        "password": "icy@owl#"
    },
    {
        "username": "wild_hawk",
        "email": "wild.hawk@gmail.com",
        "role": Role.STUDENT,
        "password": "wild@hawk#"
    },
    {
        "username": "dreamy_fish",
        "email": "dreamy.fish@gmail.com",
        "role": Role.STUDENT,
        "password": "dreamy@fish#"
    },
    {
        "username": "bright_star",
        "email": "bright.star@gmail.com",
        "role": Role.STUDENT,
        "password": "bright@star#"
    },
    {
        "username": "happy_turtle",
        "email": "happy.turtle@gmail.com",
        "role": Role.STUDENT,
        "password": "happy@turtle#"
    },
    {
        "username": "mystic_unicorn",
        "email": "mystic.unicorn@gmail.com",
        "role": Role.STUDENT,
        "password": "mystic@unicorn#"
    },
    {
        "username": "sassy_cat",
        "email": "sassy.cat@gmail.com",
        "role": Role.STUDENT,
        "password": "sassy@cat#"
    },
    {
        "username": "fiery_phoenix",
        "email": "fiery.phoenix@gmail.com",
        "role": Role.STUDENT,
        "password": "fiery@phoenix#"
    },
    {
        "username": "gentle_breeze",
        "email": "gentle.breeze@gmail.com",
        "role": Role.STUDENT,
        "password": "gentle@breeze#"
    },
    {
        "username": "daring_deer",
        "email": "daring.deer@gmail.com",
        "role": Role.STUDENT,
        "password": "daring@deer#"
    },
    {
        "username": "noble_stag",
        "email": "noble.stag@gmail.com",
        "role": Role.STUDENT,
        "password": "noble@stag#"
    },
    {
        "username": "charming_fawn",
        "email": "charming.fawn@gmail.com",
        "role": Role.STUDENT,
        "password": "charming@fawn#"
    },
    {
        "username": "zesty_lemon",
        "email": "zesty.lemon@gmail.com",
        "role": Role.STUDENT,
        "password": "zesty@lemon#"
    },
    {
        "username": "quiet_lake",
        "email": "quiet.lake@gmail.com",
        "role": Role.STUDENT,
        "password": "quiet@lake#"
    },
    {
        "username": "chilly_wind",
        "email": "chilly.wind@gmail.com",
        "role": Role.STUDENT,
        "password": "chilly@wind#"
    },
    {
        "username": "sunny_day",
        "email": "sunny.day@gmail.com",
        "role": Role.STUDENT,
        "password": "sunny@day#"
    },
    {
        "username": "lazy_sheep",
        "email": "lazy.sheep@gmail.com",
        "role": Role.STUDENT,
        "password": "lazy@sheep#"
    },
    {
        "username": "purring_kitten",
        "email": "purring.kitten@gmail.com",
        "role": Role.STUDENT,
        "password": "purring@kitten#"
    },
    {
        "username": "playful_puppy",
        "email": "playful.puppy@gmail.com",
        "role": Role.STUDENT,
        "password": "playful@puppy#"
    },
    {
        "username": "shimmering_wave",
        "email": "shimmering.wave@gmail.com",
        "role": Role.STUDENT,
        "password": "shimmering@wave#"
    },
    {
        "username": "dancing_flame",
        "email": "dancing.flame@gmail.com",
        "role": Role.STUDENT,
        "password": "dancing@flame#"
    },
    {
        "username": "twinkling_light",
        "email": "twinkling.light@gmail.com",
        "role": Role.STUDENT,
        "password": "twinkling@light#"
    },
    {
        "username": "golden_sunset",
        "email": "golden.sunset@gmail.com",
        "role": Role.STUDENT,
        "password": "golden@sunset#"
    },
    {
        "username": "radiant_rainbow",
        "email": "radiant.rainbow@gmail.com",
        "role": Role.STUDENT,
        "password": "radiant@rainbow#"
    },
    {
        "username": "mellow_moon",
        "email": "mellow.moon@gmail.com",
        "role": Role.STUDENT,
        "password": "mellow@moon#"
    },
    {
        "username": "sandy_beach",
        "email": "sandy.beach@gmail.com",
        "role": Role.STUDENT,
        "password": "sandy@beach#"
    },
    {
        "username": "rolling_hills",
        "email": "rolling.hills@gmail.com",
        "role": Role.STUDENT,
        "password": "rolling@hills#"
    },
    {
        "username": "glowing_stone",
        "email": "glowing.stone@gmail.com",
        "role": Role.STUDENT,
        "password": "glowing@stone#"
    },
    {
        "username": "frosty_peak",
        "email": "frosty.peak@gmail.com",
        "role": Role.STUDENT,
        "password": "frosty@peak#"
    },
    {
        "username": "rustic_bridge",
        "email": "rustic.bridge@gmail.com",
        "role": Role.STUDENT,
        "password": "rustic@bridge#"
    },
    {
        "username": "charming_grove",
        "email": "charming.grove@gmail.com",
        "role": Role.STUDENT,
        "password": "charming@grove#"
    },
    {
        "username": "whimsical_wind",
        "email": "whimsical.wind@gmail.com",
        "role": Role.STUDENT,
        "password": "whimsical@wind#"
    },
    {
        "username": "dappled_forest",
        "email": "dappled.forest@gmail.com",
        "role": Role.STUDENT,
        "password": "dappled@forest#"
    },
    {
        "username": "splashing_water",
        "email": "splashing.water@gmail.com",
        "role": Role.STUDENT,
        "password": "splashing@water#"
    },
    {
        "username": "mystical_fog",
        "email": "mystical.fog@gmail.com",
        "role": Role.STUDENT,
        "password": "mystical@fog#"
    },
]

if __name__ == '__main__':
    try:
        with Session() as db:
            for user in user_list:
                db.add(User(
                    username=user['username'],
                    email=user['email'],
                    password=hash_password(user['password']),
                    role=user['role'],
                ))
            db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
