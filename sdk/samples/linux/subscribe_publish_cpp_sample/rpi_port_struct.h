
#ifndef RPI_PORT_STRUCT_HPP
#define RPI_PORT_STRUCT_HPP
enum PortSetting {
	digitalOutput = 1,
	digitalInput = 2,
	analogueInput = 4,
	analogueOutput = 8,
	pwm = 16,
	spi = 32,
	serial = 64,
	i2c = 128,
};

struct RaspberryPiPort {
	int pin;
	PortSetting portSetting;
	PortSetting capability;

};



#endif