package base

func GetRecipientUserId(userId string) string {
	return userId
}

func GetComplaintId(complaintId string) string {
	return complaintId
}

func GetCurrentUserId() string {
	// todo: Get from auth service
	return "1"
}
