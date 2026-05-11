# Stored Procedure: `BPTC_Get_ThongTinBCSP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.697000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.697000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@NhomSanPhamBaoCaoID` | `int(4)` | No |
| `@NguoiLap` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Get_ThongTinBCSP]
    (
      @NgayBatDau DATETIME ,
      @NgayKetThuc DATETIME ,
      @NhomSanPhamBaoCaoID INT ,
      @NguoiLap NVARCHAR(255)
    )
AS 
    BEGIN
        DECLARE @TenBaoCao NVARCHAR(250)
        DECLARE @TenNhomSanPhamBaoCao NVARCHAR(255)
		DECLARE @BaoCaoTTSanPhamThangID INT
		PRINT CONVERT (TIME,GETDATE())
		PRINT 1
        SELECT  @TenNhomSanPhamBaoCao = TenNhomSanPhamBaoCao
        FROM    dbo.DmNhomSanPhamBaoCao
        WHERE   DmNhomSanPhamBaoCaoID = @NhomSanPhamBaoCaoID
		PRINT CONVERT (TIME,GETDATE())
        SET @TenBaoCao = @TenNhomSanPhamBaoCao + '_' + CONVERT(NVARCHAR(12), @NgayBatDau, 103)
            + '_' + CONVERT(NVARCHAR(12), @NgayKetThuc, 103) + '_' + @NguoiLap
            + '_' + CONVERT(NVARCHAR(12), GETDATE(), 113)
	
        DECLARE @NgayLap DATETIME
        SET @NgayLap = GETDATE()
        PRINT CONVERT (TIME,GETDATE())	
        PRINT 2
        INSERT  INTO dbo.BPTC_BaoCaoTTSanPhamThang
                ( TenBaoCao ,
				  NhomSanPhamBaoCaoID,
				  TenNhomSanPhamBaoCao,	
                  ThoiGianBatDau ,
                  ThoiGianKetThuc ,
                  NguoiLap ,
                  NgayLap ,
                  TrangThaiPheDuyet ,
                  NguoiPheDuyet ,
                  NgayPheDuyet ,
                  CreatedBy ,
                  CreatedAt ,
                  LastModifiedBy ,
                  LastModifiedAt ,
                  DeleteStatus ,
                  PrintStatus ,
                  RecordStatus
	          )
        VALUES  ( @TenBaoCao ,
				  @NhomSanPhamBaoCaoID,	
				  @TenNhomSanPhamBaoCao,
                  @NgayBatDau , -- ThoiGianBatDau - datetime
                  @NgayKetThuc , -- ThoiGianKetThuc - datetime
                  @NguoiLap , -- NguoiLap - nvarchar(50)
                  @NgayLap , -- NgayLap - datetime
                  0 , -- TrangThaiPheDuyet - int
                  NULL , -- NguoiPheDuyet - nvarchar(50)
                  NULL , -- NgayPheDuyet - datetime
                  @NguoiLap , -- CreatedBy - nvarchar(50)
                  @NgayLap , -- CreatedAt - datetime
                  @NguoiLap , -- LastModifiedBy - nvarchar(50)
                  @NgayLap , -- LastModifiedAt - datetime
                  0 , -- DeleteStatus - int
                  0 , -- PrintStatus - int
                  0  -- RecordStatus - int
	          )
	PRINT CONVERT (TIME,GETDATE()) 
	PRINT 3       
	SELECT @BaoCaoTTSanPhamThangID = MAX(BPTC_BaoCaoTTSanPhamThangID)	 		        
	FROM dbo.BPTC_BaoCaoTTSanPhamThang
	PRINT CONVERT (TIME,GETDATE())
	DECLARE @SQLString NVARCHAR(500)
	DECLARE @ParmDefinition NVARCHAR(500)
	PRINT CONVERT (TIME,GETDATE()) 
	PRINT 4
	--BPTC_BaoCaoTTSanPhamThang_DanhSo	 
	 SET @SQLString = N'exec dbo.BPTC_Get_BaoCaoTTSanPhamThang_DanhSo @NgayBatDau, @NgayKetThuc, @ParentID, @TenBaoCao' ;
	 SET @ParmDefinition = N'@NgayBatDau DATETIME, @NgayKetThuc DATETIME, @ParentID INT, @TenBaoCao nvarchar(250)' ;
	/* Execute the string with the first parameter value. */
	 EXECUTE sp_executesql @SQLString, @ParmDefinition, @NgayBatDau = @NgayBatDau,
		@NgayKetThuc = @NgayKetThuc, @ParentID = @BaoCaoTTSanPhamThangID,
		@TenBaoCao = @TenBaoCao ;
		PRINT CONVERT (TIME,GETDATE()) 
		PRINT 5 	
	--BPTC_BaoCaoTTSanPhamThang_ThucChay	 
	 SET @SQLString = N'exec dbo.BPTC_Get_BaoCaoTTSanPhamThang_ThucChay @NgayBatDau, @NgayKetThuc, @ParentID, @TenBaoCao' ;
	 SET @ParmDefinition = N'@NgayBatDau DATETIME, @NgayKetThuc DATETIME, @ParentID INT, @TenBaoCao nvarchar(250)' ;
	/* Execute the string with the first parameter value. */
	 EXECUTE sp_executesql @SQLString, @ParmDefinition, @NgayBatDau = @NgayBatDau,
		@NgayKetThuc = @NgayKetThuc, @ParentID = @BaoCaoTTSanPhamThangID,
		@TenBaoCao = @TenBaoCao ;
		PRINT CONVERT (TIME,GETDATE()) 
		PRINT 6
	--BPTC_BaoCaoTTSanPhamThang_ThucChay_DanhSo	 
	 SET @SQLString = N'exec dbo.BPTC_Get_BaoCaoTTSanPhamThang_ThucChay_DanhSo @NgayBatDau, @NgayKetThuc, @ParentID, @TenBaoCao' ;
	 SET @ParmDefinition = N'@NgayBatDau DATETIME, @NgayKetThuc DATETIME, @ParentID INT, @TenBaoCao nvarchar(250)' ;
	/* Execute the string with the first parameter value. */
	 EXECUTE sp_executesql @SQLString, @ParmDefinition, @NgayBatDau = @NgayBatDau,
		@NgayKetThuc = @NgayKetThuc, @ParentID = @BaoCaoTTSanPhamThangID,
		@TenBaoCao = @TenBaoCao ;
		PRINT CONVERT (TIME,GETDATE()) 
		PRINT 7
	SELECT @BaoCaoTTSanPhamThangID AS BaoCaoTTSanPhamThangID			
	
    END



```
