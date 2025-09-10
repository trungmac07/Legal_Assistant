import { refreshAccessTokenService } from "../services/login_service"

export const refreshAccessToken = async () => {
    const newToken = await refreshAccessTokenService();
    return newToken
}