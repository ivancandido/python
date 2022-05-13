from pygeocoder import Geocoder
endereco = "1700, Estrada do Capuava, Cotia"
print(Geocoder('AIzaSyADiss0AJd01kPiY1iNAsacFugHVItJBnA').geocode(endereco).coordinates)

