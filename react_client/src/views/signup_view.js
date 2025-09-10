import { useState } from "react";
import { signup } from "../controllers/signup_controller";
import AuthLayout from '../layouts/AuthLayout';
import Input from '../components/ui/Input';
import Button from '../components/ui/Button';
import { ROUTES } from '../utils/config';


const SignupView = () => {

    const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
        date_of_birth: '',
        address: '',
        gender: '',
        password: '',
        password_confirm: '',
      });
    
    
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const signupClick = async (e) => {
        e.preventDefault();
        if (
            !formData.first_name ||
            !formData.last_name ||
            !formData.email ||
            !formData.phone_number ||
            !formData.date_of_birth ||
            !formData.address ||
            !formData.gender ||
            !formData.password ||
            !formData.password_confirm
          ) 
        {
            alert('Please fill in all fields.');
            return;
        }
        else if(formData.password !== formData.password_confirm) 
            alert('Password do not match ! Please try again');
        else
        {
            const respones = await signup(formData)
           
            if ([200, 201].includes(respones.status)) {
              alert(respones.data["message"]);
              window.location.href = '/login';
            }
            
        }
        
    };
    

    return (
      <AuthLayout title="Sign Up for Focus!">
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          <div style={{ display: 'flex', gap: 12 }}>
            <Input type="text" name="first_name" placeholder="First Name" value={formData.first_name} onChange={handleChange} />
            <Input type="text" name="last_name" placeholder="Last Name" value={formData.last_name} onChange={handleChange} />
          </div>
          <Input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} />
          <Input type="tel" name="phone_number" placeholder="Phone Number" value={formData.phone_number} onChange={handleChange} />
          <Input type="date" name="date_of_birth" placeholder="Date of Birth" value={formData.date_of_birth} onChange={handleChange} />
          <textarea name="address" placeholder="Address" rows="3" value={formData.address} onChange={handleChange} style={{ width: '100%', padding: 12, border: '1px solid #b2dfdb', borderRadius: 8 }} />
          <select name="gender" value={formData.gender} onChange={handleChange} style={{ width: '100%', padding: 12, border: '1px solid #b2dfdb', borderRadius: 8 }}>
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
          <Input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} />
          <Input type="password" name="password_confirm" placeholder="Confirm Password" value={formData.password_confirm} onChange={handleChange} />
          <Button type="submit" onClick={signupClick}>Sign Up</Button>
          <p style={{ marginTop: 12, fontSize: 14, color: '#555' }}>
            Already have an account? <a href={ROUTES.login} style={{ color: '#007bff', textDecoration: 'none' }}>Login</a>
          </p>
        </div>
      </AuthLayout>
    );
    };
    
  
  export default SignupView ;