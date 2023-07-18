import React from 'react';
import GooglePlacesAutocomplete from 'react-google-places-autocomplete';

function SearchBox({ onPlaceSelect }) {
  return (
    <GooglePlacesAutocomplete
      onSelect={(selectedPlace) => onPlaceSelect(selectedPlace.place_id)}
    />
  );
}

export default SearchBox;
