
from gpiozero import Servo
from gpiozero.pins.lgpio import LGPIOFactory
import math

LEFT_PIN = 18
RIGHT_PIN = 19

factory = LGPIOFactory()

left_servo = Servo(LEFT_PIN, pin_factory=factory)
right_servo = Servo(RIGHT_PIN, pin_factory=factory)

try:
    # 두 서보모터 중앙 정렬
    left_servo.value = 0
    right_servo.value = 0

    print("Servo control started.")
    print("Commands: l -1~1, r -1~1, q")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "q":
            break

        parts = command.split()

        if len(parts) != 2:
            print("Example: l -0.5 or r 0.5")
            continue

        side = parts[0]

        try:
            value = float(parts[1])
        except ValueError:
            print("Invalid number.")
            continue

        # -1 ~ 1 범위 검사
        if not math.isfinite(value) or not -1 <= value <= 1:
            print("Enter a value between -1 and 1.")
            continue

        # 왼쪽 서보 제어
        if side == "l":
            left_servo.value = value
            print(f"Left servo: {value}")

        # 오른쪽 서보 제어
        elif side == "r":
            right_servo.value = value
            print(f"Right servo: {value}")

        else:
            print("Use l or r.")

except KeyboardInterrupt:
    print("\nStopped.")

finally:
    left_servo.close()
    right_servo.close()
    factory.close()
