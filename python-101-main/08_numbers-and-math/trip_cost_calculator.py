'''Receive following args:

- kilometers to drive
- liters-per-kilometer usage of the car
- price per liter of fuel

Calculate cost of trip, display to user
'''
import click


trip_destination = str(input('Where are you headed? '))
print()


@click.command()
@click.option('--distance', prompt=True, type=int, help='Distance in km')
@click.option('--liters', prompt=True, type=float, help='Liters per km usage of car')
@click.option('--fuel_price', prompt=True, type=float, help='Price per liter of fuel')

def get_driver_information(distance, liters, fuel_price):
    ctx = click.get_current_context()

    try:

        trip_total_cost = distance / liters * fuel_price

        click.echo(f'The total cost of your trip to {trip_destination.title()} is €{trip_total_cost:.2f}')

    except ZeroDivisionError as er:
        print(f'Run-time error: {er}')
        click.echo(ctx.get_help())
        ctx.exit()


if __name__ == "__main__":

    get_driver_information()

