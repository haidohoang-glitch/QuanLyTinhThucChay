# Stored Procedure: `OtpSetting_List_All_Staff`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-26 10:46:13.490000
- **Ngày sửa cuối**: 2014-11-26 10:46:13.490000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[OtpSetting_List_All_Staff]	
AS
BEGIN

	SELECT 
	T.NhanSuSoYeuLyLichID, T.HoVaTen AS FullName, T.Email, T.Mobile, T.OxUserID, T.UserName
	FROM(
	SELECT  
	A.OxUserID
	,A.UserName
	,C.NhanSuSoYeuLyLichID
	,C.HoVaTen
	,E.DmPhongBanID
	,E.TenPhongBan
	,F.DmBoPhanID
	,F.TenBoPhan
	,G.DmNhomID
	,G.TenNhom
	,
	case isnull(replace(A.Email,' ',''),replace(C.Email,' ','')) 
	WHEN '' THEN replace(C.Email,' ','')
	ELSE isnull(replace(A.Email,' ',''),replace(C.Email,' ',''))
	end AS Email
	,
	case isnull(replace(A.MobileNumber,' ',''),replace(C.Mobile,' ','')) 
	WHEN '' THEN replace(C.Mobile,' ','')
	ELSE isnull(replace(A.MobileNumber,' ',''),replace(C.Mobile,' ','')) 
	end AS Mobile

	FROM ABM_Security.dbo.OxUser A
	LEFT JOIN ABM_Security.dbo.NhanSuQuyenNguoiDung B ON A.OxUserID = B.OxUserREF
	LEFT JOIN ABM_Security.dbo.NhanSuSoYeuLyLich C ON C.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF
	LEFT JOIN ABM_Security.dbo.NhanSuQuaTrinhCongTac D ON D.NhanSuSoYeuLyLichREF = C.NhanSuSoYeuLyLichID
	LEFT JOIN ABM_Security.dbo.DmPhongBan  E ON E.DmPhongBanID = D.DmPhongBanREF
	LEFT JOIN ABM_Security.dbo.DmBoPhan F ON F.DmBoPhanID = D.DmBoPhanREF
	LEFT JOIN ABM_Security.dbo.DmNhom G ON G.DmNhomID = D.DmNhomREF
	WHERE
	C.NgayNghiViec IS NULL
	AND D.[Active] = 1
	)T
	WHERE
	T.Mobile IS Not NULL 
	AND T.Mobile <> ''
END

```
