#!/usr/bin/python3

import time
import math

import config
import utils

from PIL import Image, ImageFont, ImageDraw


def update_startup_screen():
    """Show startup screen on eInk Display
    """
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (20, 10),
        "Welcome to the",
        fill=config.BLACK,
        font=utils.create_font("freemono", 18),
    )
    draw.text(
        (10, 20),
        "LightningATM",
        fill=config.BLACK,
        font=utils.create_font("sawasdee", 30),
    )
    draw.text(
        (7, 75),
        "- please insert coins -",
        fill=config.BLACK,
        font=utils.create_font("freemono", 14),
    )

    display_image(image, True)


def update_qr_request():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (25, 10),
        "Please scan",
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )
    draw.text(
        (10, 30),
        "your invoice in",
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )


    for i in range(0, 3):
        draw.text(
            (80, 45),
            str(3 - i),
            fill=config.BLACK,
            font=utils.create_font("freemono", 50),
        )

        display_image(image)
        draw.rectangle((75, 50, 115, 90), fill=config.WHITE, outline=config.WHITE)
        time.sleep(1)


def update_lnurl_qr(qr_img):
    image, width, height, draw = init_screen(color=config.BLACK)
    draw = ImageDraw.Draw(image)
    draw.bitmap((0, 0), qr_img, fill=config.WHITE)
    draw.text(
        (110, 25),
        "Scan to",
        fill=config.WHITE,
        font=utils.create_font("freemonobold", 16),
    )
    draw.text(
        (110, 45),
        "receive",
        fill=config.WHITE,
        font=utils.create_font("freemonobold", 16),
    )
    draw.text(
        (110, 65),
        "by LNURL",
        fill=config.WHITE,
        font=utils.create_font("freemonobold", 16),
    )

    display_image(image, True)


def update_qr_failed():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (25, 10),
        "Scanning...",
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )
    draw.text(
        (25, 30),
        "Scan failed.",
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )
    draw.text(
        (25, 50),
        "Try again.",
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )

    display_image(image, True)


def update_payout_screen():
    """Update the payout screen to reflect balance of deposited coins.
    Scan the invoice??? I don't think so!
    """
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (15, 30),
        str(math.floor(config.SATS)) + " sats",
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )
    draw.text(
        (15, 50),
        "on the way!",
        fill=config.BLACK,
        font=utils.create_font("freemono", 15),
    )

    display_image(image, True)

    # scan the invoice
    # TODO: I notice this is commented out, I presume this function should _not_ be
    #   scanning a QR code on each update?
    # config.INVOICE = qr.scan()


def update_payment_failed():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (15, 10),
        "Payment failed!",
        fill=config.BLACK,
        font=utils.create_font("freemono", 19),
    )
    draw.text(
        (25, 45),
        "Please contact",
        fill=config.BLACK,
        font=utils.create_font("freemono", 17),
    )
    draw.text(
        (45, 65), "operator.", fill=config.BLACK, font=utils.create_font("freemono", 17)
    )

    display_image(image, True)


def update_thankyou_screen():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (15, 10),
        "Enjoy your new",
        fill=config.BLACK,
        font=utils.create_font("freemono", 19),
    )
    draw.text(
        (40, 35),
        "satoshis!!",
        fill=config.BLACK,
        font=utils.create_font("freemono", 19),
    )
    draw.text(
        (15, 70),
        "#bitcoin #lightning",
        fill=config.BLACK,
        font=utils.create_font("freemono", 14),
    )

    display_image(image, True)
    time.sleep(5)


def update_nocoin_screen():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (15, 10),
        "No coins added!",
        fill=config.BLACK,
        font=utils.create_font("freemono", 19),
    )
    draw.text(
        (25, 45),
        "Please add",
        fill=config.BLACK,
        font=utils.create_font("freemono", 17),
    )
    draw.text(
        (45, 65),
        "coins first.",
        fill=config.BLACK,
        font=utils.create_font("freemono", 17),
    )

    display_image(image, True)


def update_lnurl_generation():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (30, 20),
        "Generating",
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )
    draw.text(
        (10, 40),
        "QR code to scan",
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )

    display_image(image)


def update_shutdown_screen():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (20, 10),
        "ATM turned off!",
        fill=config.BLACK,
        font=utils.create_font("freemono", 18),
    )
    draw.text(
        (25, 45),
        "Please contact",
        fill=config.BLACK,
        font=utils.create_font("freemono", 17),
    )
    draw.text(
        (45, 65), "operator.", fill=config.BLACK, font=utils.create_font("freemono", 17)
    )

    display_image(image, True)


def update_lntxbot_scan():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (35, 20),
        "Please scan",
        fill=config.BLACK,
        font=utils.create_font("freemono", 18),
    )
    draw.text(
        (33, 40),
        "your lntxbot",
        fill=config.BLACK,
        font=utils.create_font("freemono", 18),
    )
    draw.text(
        (35, 60),
        "credentials.",
        fill=config.BLACK,
        font=utils.create_font("freemono", 18),
    )

    display_image(image, True)
    time.sleep(2)


def update_lntxbot_balance(balance):
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (45, 15),
        "Success!!",
        fill=config.BLACK,
        font=utils.create_font("freemonobold", 20),
    )
    draw.text(
        (10, 45),
        "Your current balance:",
        fill=config.BLACK,
        font=utils.create_font("freemono", 15),
    )
    draw.text(
        (45, 65),
        str("{:,}".format(balance)) + " sats",
        fill=config.BLACK,
        font=utils.create_font("freemono", 18),
    )

    display_image(image, True)
    time.sleep(3)


def update_amount_screen():
    """Update the amount screen to reflect new coins inserted
    """
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (11, 10),
        str("{:,}".format(math.floor(config.SATS))) + " sats",
        fill=config.BLACK,
        font=utils.create_font("freemono", 27),
    )
    draw.text(
        (13, 37),
        "%.2f" % round(config.FIAT, 2) + " " + config.conf["atm"]["cur"].upper(),
        fill=config.BLACK,
        font=utils.create_font("freemono", 19),
    )
    draw.text(
        (11, 60), "Rate", fill=config.BLACK, font=utils.create_font("freemono", 14),
    )
    draw.text(
        (60, 60),
        "= " + str(math.floor(config.SATPRICE)) + " sats/cent",
        fill=config.BLACK,
        font=utils.create_font("freemono", 14),
    )
    draw.text(
        (11, 75), "Fee", fill=config.BLACK, font=utils.create_font("freemono", 14),
    )
    draw.text(
        (60, 75),
        "= "
        + config.conf["atm"]["fee"]
        + "% ("
        + str(math.floor(config.SATSFEE))
        + " sats)",
        fill=config.BLACK,
        font=utils.create_font("freemono", 14),
    )

    display_image(image, True)


def update_blank_screen():
    image, width, height, draw = init_screen(color=config.WHITE)
    display_image(image, True)


def menu_screen():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (20, 16), "►", fill=config.BLACK, font=utils.create_font("freemono", 20),
    )
    draw.text(
        (40, 20), "Menu 1", fill=config.BLACK, font=utils.create_font("freemono", 20),
    )
    draw.text(
        (40, 40), "Menu 2", fill=config.BLACK, font=utils.create_font("freemono", 20),
    )

    display_image(image)

    while config.PUSHES <= 2:
        print(config.PUSHES)
        time.sleep(2)


def init_screen(color):
    """Prepare the screen for drawing and return the draw variables
    """
    # image = Image.new("1", config.PAPIRUS.size, color)
    image = Image.new("1", (config.WAVESHARE.height, config.WAVESHARE.width), color)
    # Set width and height of screen
    width, height = image.size
    # prepare for drawing
    draw = ImageDraw.Draw(image)
    return image, width, height, draw


def display_image(image, full_update=False):
    """Show an image on the display
    """

    # config.PAPIRUS.display(image)
    config.WAVESHARE.init()

    if full_update:
        # config.PAPIRUS.update()
        config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))
    else:
        # config.PAPIRUS.partial_update()
        # config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))
        config.WAVESHARE.DisplayPartial(config.WAVESHARE.getbuffer(image))

