import wpilib
import wpilib
from wpilib.interfaces import GenericHID
import rev


class KodyBot(wpilib.TimedRobot):

    def robotInit(self):
        """self.rgt_front = rev.SparkMax(2, rev.MotorType.kBrushless)
        self.lft_front = rev.SparkMax(3, rev.MotorType.kBrushless)"""

        self.rgt_front = wpilib.PWMTalonFX(0)
        self.lft_front = wpilib.PWMTalonFX(1)

        self.joy = wpilib.XboxController(0)

        self.rgt_front.setInverted(True)
        self.lft_front.setInverted(False)

    def autonomousInit(self):
        self.rgt_front.set(0.2)
        self.lft_front.set(0.2)

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.rgt_front.set(self.joy.getRawAxis(3))
        self.lft_front.set(self.joy.getRawAxis(3))

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(KodyBot)



