#include "json.hpp"
#include <iostream>

int main() {
  using nlohmann::json;
  json j = { {"Hello", "World"} };
  for (json::iterator it = j.begin(); it != j.end(); ++it) {
    std::cout << it.key() << " " << it.value() << '\n';
  }
}