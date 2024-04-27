package token

type User struct {
	Username         string `json:"username"`
	Phone            string `json:"user_phone"`
	Other            string `json:"user_other"`
	ProfileImage     string `json:"user_profile_image"`
	Role             string `json:"role"`
	ComplaintsSolved int    `json:"user_complaints_solved"`
	Description      string `json:"user_description"`
	Place            string `json:"user_place"`
	PlaceGeocode     string `json:"user_place_geocode"`
	Notifications    int    `json:"user_notifications"`
	Slug             string `json:"slug"`
}
