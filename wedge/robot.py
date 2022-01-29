#!/usr/bin/env python3
"""
    This is a demo program showing how to use Mecanum control with the
    MecanumDrive class.

    Since the team has decided to build a wedge, this code is going to
    have to be modified to use only three motors.
"""

import wpilib
import rev
from wpilib.drive import MecanumDrive


class MyRobot(wpilib.TimedRobot):
    # Channels on the roboRIO that the motor controllers are plugged in to
    frontLeftChannel = 2
    rearLeftChannel = 3
    frontRightChannel = 1
    rearRightChannel = 0

    # The channel on the driver station that the joystick is connected to
    joystickChannel = 0

    def robotInit(self):
        """Robot initialization function"""
        self.frontLeftMotor = rev.CANSparkMax(self.frontLeftChannel, kBrushless)
        self.rearLeftMotor = rev.CANSparkMax(self.rearLeftChannel, kBrushless)
        self.frontRightMotor = rev.CANSparkMax(self.frontRightChannel, kBrushless)
        self.rearRightMotor = rev.CANSparkMax(self.rearRightChannel, kBrushless)

        # invert the left side motors
        self.frontLeftMotor.setInverted(True)

        # you may need to change or remove this to match your robot
        self.rearLeftMotor.setInverted(True)

        self.drive = MecanumDrive(
            self.frontLeftMotor,
            self.rearLeftMotor,
            self.frontRightMotor,
            self.rearRightMotor,
        )

        self.drive.setExpiration(0.1)

        self.stick = wpilib.Joystick(self.joystickChannel)

    def teleopInit(self):
        self.drive.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with Mecanum drive."""
        # Use the joystick X axis for lateral movement, Y axis for forward movement, and Z axis for rotation.
        # This sample does not use field-oriented drive, so the gyro input is set to zero.
        self.drive.driveCartesian(
            self.stick.getX(), self.stick.getY(), self.stick.getZ(), 0
        )


if __name__ == "__main__":
    wpilib.run(MyRobot)
