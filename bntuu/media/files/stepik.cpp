#include <iostream>

// Базовый класс транспортного средства
class Transport {
public:
    virtual void move() = 0;
};

// Класс автомобиля
class Car : public Transport {
public:
    void move() override {
        std::cout << "Автомобиль движется по дороге." << std::endl;
    }
};

// Класс самолета
class Airplane : public Transport {
public:
    void move() override {
        std::cout << "Самолет летит в небе." << std::endl;
    }
};

// Класс корабля
class Ship : public Transport {
public:
    void move() override {
        std::cout << "Корабль плывет по воде." << std::endl;
    }
};

// Абстрактный класс фабрики транспортных средств
class TransportFactory {
public:
    virtual Transport* createTransport() = 0;
};

// Фабрика автомобилей
class CarFactory : public TransportFactory {
public:
    Transport* createTransport() override {
        return new Car();
    }
};

// Фабрика самолетов
class AirplaneFactory : public TransportFactory {
public:
    Transport* createTransport() override {
        return new Airplane();
    }
};

// Фабрика кораблей
class ShipFactory : public TransportFactory {
public:
    Transport* createTransport() override {
        return new Ship();
    }
};

int main() {
    // Создание фабрик
    TransportFactory* carFactory = new CarFactory();
    TransportFactory* airplaneFactory = new AirplaneFactory();
    TransportFactory* shipFactory = new ShipFactory();

    // Создание транспортных средств с использованием фабричного метода
    Transport* car = carFactory->createTransport();
    Transport* airplane = airplaneFactory->createTransport();
    Transport* ship = shipFactory->createTransport();

    // Вызов метода движения для каждого транспортного средства
    car->move();
    airplane->move();
    ship->move();

    // Освобождение памяти
    delete car;
    delete airplane;
    delete ship;
    delete carFactory;
    delete airplaneFactory;
    delete shipFactory;

    return 0;
}