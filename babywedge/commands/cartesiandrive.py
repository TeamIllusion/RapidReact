# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import typing
import commands2
from subsystems.drivetrain import Drivetrain


class CartesianDrive(commands2.CommandBase):
    def __init__(
        self,
        drive: Drivetrain,
        forward: typing.Callable[[], float],
        sideways: typing.Callable[[], float],
        rotation: typing.Callable[[], float],
    ) -> None:
        """Creates a new CartesianDrive. This command will drive your robot according to the speed supplier
        lambdas. This command does not terminate.

        :param drivetrain:  The drivetrain subsystem on which this command will run
        :param forward:     Callable supplier of forward/backward speed
        :param sideways:    Callable supplier of left/rigt speed
        :param rotation:    Callable supplier of rotational speed
        """
        super().__init__()

        self.drive = drive
        self.forward = forward
        self.sideways = sideways
        self.rotation = rotation

        self.addRequirements([self.drive])

    def execute(self) -> None:
        self.drive.driveCartesian(self.forward(), self.sideways(), self.rotation())
