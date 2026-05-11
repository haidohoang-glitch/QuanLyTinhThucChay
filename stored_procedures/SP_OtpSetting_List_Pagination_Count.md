# Stored Procedure: `OtpSetting_List_Pagination_Count`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-26 10:46:13.500000
- **Ngày sửa cuối**: 2014-11-26 10:46:13.500000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@LstId` | `nvarchar` | No |
| `@PBN` | `int(4)` | No |
| `@TypeId` | `int(4)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- OtpSetting_List_Pagination '100674, 102131', 0, 0, 1, 10, 1
-- OtpSetting_List_Pagination '', 8, 1, 1, 1000, 1
-- OtpSetting_List_Pagination_Count  '985', 0, 0
-- =============================================
CREATE PROCEDURE [dbo].[OtpSetting_List_Pagination_Count]
	@LstId		NVARCHAR(MAX) = '',
	@PBN		INT,
	@TypeId		INT					
AS
BEGIN
	DECLARE
		@STMT	NVARCHAR(MAX), -- SQL to execute                     
		@Filter NVARCHAR(MAX) = ' '	   
	


			IF (@TypeId = 1)
				SET @Filter += ' AND E.DmPhongBanID = ' +  CONVERT(NVARCHAR(9), @PBN)
			ELSE IF (@TypeId = 2)
				SET @Filter += ' AND F.DmBoPhanID = ' +  CONVERT(NVARCHAR(9), @PBN)
			ELSE IF (@TypeId = 3)
				SET @Filter += ' AND G.DmNhomID = ' +  CONVERT(NVARCHAR(9), @PBN)
		
			IF(@LstId <> '')
				SET @Filter += ' AND C.NhanSuSoYeuLyLichID IN (' + @LstId + ')'	      	            
				SET @STMT =
   						'SELECT count(*) AS MaxRecords
							
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
							and A.MobileNumber is not null and A.MobileNumber <> ''''
							and C.Mobile is not null and C.Mobile <> '''' 
					' + @Filter


				                                                      
    PRINT (@STMT)
                        
    EXEC (@STMT)                 -- return requested records   
END

```
