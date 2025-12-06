import './globals.css'

export const metadata = {
    title: 'BMO Agent Task System',
    description: 'Submit tasks and let the agent decide which tool to use',
}

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body>{children}</body>
        </html>
    )
}